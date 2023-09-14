.. _Sieve_in_rPython:

====================
The Sieve in RPython
====================

.. post:: 		
   :category:  RPython, Experiment, rough
   :tags: Castle, WorkshopTools

   Before implementing an :ref:`RPython backend <rPY>`, a short study of `RPython
   <https://rpython.readthedocs.io/en/latest/>`__ is made, including implementing  :ref:`Castle-TheSieve` in RPython.
   It’s like a hand-compiled RPython variant, following the approach as described in the :ref:`Jinja rendering study
   <QN_EventTemplate>`), for the :ref:`CC2CPy backend <CC2Cpy>`.


   Writing RPython isn’t too complicated for someone with a C-background. But making the code pass the RPython compiler
   can be tricky. Both, as just added statements can interfere with existing code -- when that isn’t “static enough”, new code
   can trigger compile errors in old, tested code! And because the RPython compiler isn’t that great in giving helpful info.
   |BR|
   It feels like old-style debugging: *try-and-error*, remove-and-enable-lines, one-at-a-time until one
   understands and it becomes easy to fix...

   This blog is both to share some RPython experience and to study the patterns that are needed to generate RPython
   code to implement the Castle-Compiler.

Code
****

Below we show some (manually written) code as if it is hand-compiled -- using roughly the same approach as in the
:ref:`CC2Cpy <CC2Cpy>` approach.
|BR|
I had two objectives: (a) make it (functional) work in RPython, and (b) find the patterns to automate.

Definitions
============

In Castle, you use Events, Protocols and Components (to name a few), all will result in some data structures
[#dataclasses]_  that define them: build-in classes that are (statically) instantiated.
|BR|
This part is easy to automate.

.. include:: ./RPython-definitions.irst

Generated code
===============

Each *(Castle)* component results in a (*RPython*) Class, that contain all code for that component. As (R)Python classes
are also namespaces, the names of (e.g) the even-handlers become shorter; there is no need to put the component-name in
the method-name. But in general we follow the structure as in the :ref:`CC2Cpy<CC2Cpy>` approach.

Components
----------

A (Castle) Component becomes a subclass of ``CC_B_Component``, this (abstract) base-class provides (currently, mostly)
some debugging support. Subclasses should override the ``_debug_attr_()`` method, that returns *(not print)* a string
with ``name=value`` pairs for debug-printing.

The initialiser is split in ``__init__()`` and ``_castle_init()``; the later implements (generates code for) the
Castle-init function, and is called by ``__init__()`` [#init]_.

Roughly each protocol-event for each port (aka a Eventhandler) results in a (R)Python method, as do data- (and other)
handlers, and internal functions.

DispatchTables
--------------

Every (input) port can trigger several eventhandlers (or data-/stream-/... handlers), as an (event) protocol can have
multiple events. Therefore, a component has an (event) DispatchTable per port [#activePort]_.

Every DispatchTable is an *array* (python: List) with the same size as the number of events in the corresponding
Protocol (which is static at compile-time) -- including the inherited events [#arbitrary]_.

Examples
---------

.. include:: ./RPython-generated.irst

XXXX


Templating
**********

Below we show some Jinja(s) templates, in the style of :ref:`QN_EventTemplate` (for the :ref:`CC2Cpy` backend).

XXX
===

Eventhandlers
-------------

As we use (R)Python namespaces (modules, classes), the generated names for the eventhandlers becomes shorter (than in
C).

.. code-block:: jinja

   {%macro event_handler(compName, protocol, event, portName) 
      {{protocol{}_{{event}}__{{portName}}
   {%- endmacro %}
   {# compName is not used/needed, as the method is in the `compName` class #}


------------

.. seealso::

   * https://osdn.net/users/albertmietus/pf/TryOut_PyPy-and-Rpython (SLOW!)
     |BR|
     My collection of small rpython demos, and typical Python-code that is not RPython ..
   * https://osdn.net/users/albertmietus/pf/CC_Sieve_in_rPython/wiki/FrontPage (SLOW)
     |BR|
     The code used for in study.

.. rubric:: Footnotes

.. [#dataclasses]
   To implement them `dataclasses <https://docs.python.org/3/library/dataclasses.html>`__ would be natural. They are,
   however, introduced in *Python-3.7*. As RPython is a Python-2.7 subset, they are not available.

.. [#init]
   Possible, it would be better to have 3 init functions. Now the (generated) `__init__`, calls both the `__init__` of the
   base-component/class and the `_castle_init` of the own class.
   |BR|
   This results that all Caste-init code is called, mixed with build-in/generated init code.

   However, for now this approach is used. Remomber: the goal in generated-code; which has different demands on
   maintainability.

.. [#activePort]
   We could implement this by making the ports “active”; a (R)Python class with implements an method for each event --
   then we use the DispatchTable of Python-itself. However, that port-method needs to call a method in the
   ComponentClass -- which name is not statically determined.
   |BR|
   In (normal) Python, this is possible using introspection. That feature is however not allowed in RPython.

   As all code is generated, it is still possible -- we can generate a port-method that calles a component-method, as we
   know the name of the latter during (Caste) compile-time. But is that better?
   |BR|
   At the moment, we believe a table-approach doing the same thing directly is better!

.. [#arbitrary]
   In this example, we use some arbitrary number (like 6, 7) of “dummy” inherited events for all Protocols.
