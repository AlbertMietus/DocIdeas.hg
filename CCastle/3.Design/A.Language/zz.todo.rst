TODO Language design
********************

.. _Protocol-SlowStart:

SlowStart (Language Design, ToDo)
==================================

This is part of the Congestion Avoidance concept.

.. note:: In a draft version of the docs we used “FastGrow”, but SlowStart seems a better ter,

.. todo::

   * Design a “standard base/pod protocol `SlowStart`, that can be used as base for ``SimpleSieve`` to solve the
     `Castle-Heisenbug`.

   .. _doc-SlowStart:

   * Document (how to use) this document too


.. seealso::
   * :ref:`Castle-Heisenbug`
   * :ref:`Castle-TheSieve`
   * https://en.wikipedia.org/wiki/TCP_congestion_control
   * https://en.wikipedia.org/wiki/TCP_congestion_control#Slow_start


.. _Rewriters:

Rewriters (TODO)
================

**Rewriters** are a bit like `@decorator` in python (before a class/function), and the @meta-functions in cpp2 (after
the class). The act as compiler “plugins” (likje CPP2), as can be written by a normal user (like in Python).

The “expand” (or “generate”) code) during compiling -- typically at AST (actually: :ref:`AIGR`) level

.. todo:: Design the @Rewriters
