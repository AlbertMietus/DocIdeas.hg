TODO Workshop design
********************

Trebuchet
=========

*“The Trebuchet”* is the working-title of `Mutation testing <https://en.wikipedia.org/wiki/Mutation_testing>`_ tool for Castle; to be written in castle.

The (first) ideas is to not modify the code-files (as many tools do), but to read those files into parse-tre (or in an ATS) and modify that one. It should execute  (much) faster, but more important: I hate it when tools change my files -- and my editor doesn't like it either

.. tip:: For MutationTestTool builders:

   * Plz do not, *never*, touch the files!
   * Make a virtual, “ram-based” temp-disk, copy all files to there and modify & test there. It also a lot faster!


.. _simulation :

Simulation/Verification (todo)
==============================

.. use:: Simulate & Verify all possible event-orders
   :ID: U_Tools_EventOrder

   To prevent :ref:`Castle-Heisenbug`, Castle should come with a tools to

   - Simulate “other” event-orders (show it’s effect to the user)
   - Verify that “any” event-order results in a logical & correct result.

   .. seealso:: “:ref:`Dezyne`” has such a tool



FSM details to remember
=======================

.. impl::  FSM Actions become before state-updates
   :ID: FSM_AbS
   :links: U_FSM_Syntax, U_FSM_extensions

   When implementing a FSM (:ref:`Rewriters`) actions and state-updates need to be in the right order; actions come
   before state-updates.

   When using “More & Mealy” actions, and/or hierarchically FSM’s it become a bit more complicated. But order is clearly
   described and easy..

   .. seealso::    https://en.wikipedia.org/wiki/UML_state_machine#Transition_execution_sequence

.. note:: For NFA’s this is even more complicated.
   The order is clear, but as a NFA has to be rewritten in a DFA, we have to be extra carefull to keep the same order.

   Probably, this is not even possible in general. When possible, the “compiler” should do it. When not, it should give
   a warning (or error, on request) and use an heuristic.
