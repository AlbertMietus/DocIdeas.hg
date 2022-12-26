.. include:: /std/localtoc.irst

.. _Castle-Heisenbug:

======================
Heisenbug (start/DRAF)
======================


.. post::
   :category: CastleBlogs, Castle DesignStudy
   :tags: Castle, DRAFT

   In Castle, one can dynamically connect components and send “events” over those connections. Typically this is done as
   an action on an incoming message (see: :ref:`CCC-Actors`). Depending on ‘:ref:`TheMachinery`’, those events can be
   queued and result in a beautiful Heisenbug.

   Before we give a simple example, let’s explain the Heisenbug first.
   |BR|
   Later, we continue with a generic solution (todo:-)


What is e Heisenbug?
=======================

The heisenbug is named to Werner Heisenberg, who described the “observer effect”: when you look closely, the behavior
changes. The same can happen to software (bugs). The behavior apparently changes when you study -or slightly adjust-
that code.  Often this is due (small) changes in timing; possibly even in generated code. Therefore old (oldfashioned),
sequential code on slow CPU’s is less likely to have heisenbugs then concurrent code on fast multi-core systems. It’s
also common in threaded programs.

The sieve goes wrong
--------------------

Also my standard Caste demo ‘Sieve of Eratosthenes’ can suffer from this issue. The initial version did work for years,
and failed horrible when another “machinery” was used.




 https://en.wikipedia.org/wiki/Heisenbug

..  LocalWords:  heisenbugs, heisenbug
