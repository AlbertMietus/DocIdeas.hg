.. sidebar:: On this page
   :class: localtoc

   .. contents::
      :depth: 6
      :local:
      :backlinks: none

.. _ADR0002:

================================================
ADR_0001: When To `Bundle` (Calling Conventions)
================================================

.. adr:: Calling Conventions & Bundling (RPY version)
   :ID: ADR_0002
   :Status: Seed

Context and Problem Statement
=============================

CCastle, has several kind of “callables”. Some behave more like normal methods and functions. But the “connected
components” abstraction is new, and demands some extra care when implementing.
|BR|
In this ADR we  focus exclusively on the RPY-writer. But we expect other writers may have similar issues -- if so, that
will be described in other ADRs.

For simplicity, we focus below on :class:`EventHandler`\s. But it will be equally valid for other kind of
:class:`Handler`\s.
|BR|
Notice, that this ADR describes an implementation detail only.  Which is completely hidden inside the  `machinery of an
`writer`. Still it architectural relevant: the generated code for calling a function and implementing it should
match. Besides, as it is code that is (potentially) executed for every call, it will impact the executing speed.
|BR|
To make it even more intricate, the generated RPython code may be optimized by both the RPY-translator (who generated
C-code), and the C-compiler. So, we only need to generate code, that can/will be optimized to perfect code.


The `machinery`
----------------

In CCastle, components can send event to other components via “connected ports.” To deal with that, the receiving
component has ``EventHandlers``.  In RPY, that is a Python-callable, that is called via an `DispatchTable`. That is,
basically, a mapping from (event-) names to methods.

As RPython is *restricted*, all signatures of those “handler-methods” have to be similar. This implies the same number
of parameters, with comparable types. Whereas the signatures of the Castle handler (aka ‘CC-handlers’) are not.
|BR|
So, the ‘machinery’ need to convent the CC-calling convention to a RPY-calling convention. This is managed by the (a)
:class:`Bundler`.

With the :class:`NativeBundler` all (positional) CC-parameters are “packed” into an `List` and each parameter is “boxed”
into a :class:`CC_B_Value`. This is restricted enough for RPython. (For named parameter, it a bit more complicated, but
similar --- for simplicity, we will focus on positional one only)


Methods and classic functions
------------------------------

Inside a component, fun

C/P1
----


C/P2
----


C/P3
----

Challenges
==========


Decision Drivers
----------------


Considered Options
==================

Opt 1
---------------

Opt 2
---------------

Opt 3
---------------

...

Outcome
=======

See :need:`ADR_0002` (above) for main resolution.

Consequences
------------

*
*

..  LocalWords:  callables ADR
