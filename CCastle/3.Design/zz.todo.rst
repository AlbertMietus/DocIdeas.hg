TODO (Design)
*************

Tree as std data-structure
==========================

.. todo::

   * .. seealso: :ref:`matching-statements`

   * Allow (aside of trees), also non-cyclic graps?

   * Allow (local) “links” in the tree

     - ala html: a/href
     - ala xlm: XLINK
     - Use XPATH/CSS alike syntax
     - Use ‘id’

Multiple Inheritance (for components and such)
==============================================

The idea is to allow multiple inheritance in the same way/concept as Python does. And use it’s MRO
(https://docs.python.org/3/tutorial/classes.html#multiple-inheritance) algoritm. This applies to components, but
possible at other places too

.. resolution::  No MI in first compilers
   :ID: Tools_No_MultipleInheritance-in-1compiler

   The first compilers (and other tools) will not (does not need to) support multiple inheritance.

   Although the language design should allow it, those compilers can handle it as if only single inheritance is allowed
   and give “Not supported syntax error”

.. _TheMachinery:

The Machinery (ToDo)
====================

The CC-concept has abstracted the communication between components, by using ports, connections, and protocols. A
protocol is a  “horizontal” interface: two port can be connected when they share the same protocol.
|BR|
There is however, also a “vertical” interface. This abstracted in “The Machinery” in Castle, and hidden for the typical
developer.

When two components are connected with a (shared) protocol, they “speak” the samen language. However to exchange data,
more details are needed on how this is done technically: can they use shared memory?  Or are they (only) connected by a
network? Possible, the low-level bit-representation do differ, or ...

When a Castle-programs makes a connection, some “machinery” is inserted, at a more detailed level. The data of the
sending-component in transferred down, adapted to a level where the physical exchange can happen, and transferred up
again such that the receiving-component can handle it.
|BR|
Often multiple “machineries” are possible; they offer the same services, but with other cost (as delays etc). Or with
other benefits; like the ability to “transfer over the wire”.

Some example machineries
------------------------

.. _Machinery-DirectCall:

DirectCall
~~~~~~~~~~

This is a very trivial machinery focusing on events. Each event is basically translated into a function-call. The event
of the sender is converted to an event-handle in the receiver (this is a static lookup during compiling). And that is
executed.

It works great for simple single-threaded (small) applications

.. _Machinery-LibDispatch:

LibDispatch
~~~~~~~~~~~

With LibDispatch (see: :ref:`BC-libdispatch`) events are basically *queued* to be executed on the next available thread;
where the OS (or: the implementation of libdispatch) is responsable to threads, queues etc.

It enables parallel execution, as thread and multiple core are possible.

DDS (study)
~~~~~~~~~~~

It sounds like a great idea to use DDS as a machinery, to allow components to “talks” over the network. Details have tp
be studied however.
