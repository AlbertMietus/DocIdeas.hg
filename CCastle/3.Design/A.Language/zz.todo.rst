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

**Rewriters** are a bit like `@decorator` in python (before a class/function), and ``@meta-functions`` in *CPP2* (after
the class). They take a function (or class/component/...) written in  “compact” CCastle-code, and *rewrite* it into more
specific, general CCastle-Code.

You can see them as “compiler plugins” (like in CPP2) --see: :ref:`Transformers`--, but can be developed by typical (CCastle) programmers.

The “expand” (or “generate”) code) during compiling -- typically at AST (actually: :ref:`AIGR`) level

.. todo:: Design the @Rewriters
