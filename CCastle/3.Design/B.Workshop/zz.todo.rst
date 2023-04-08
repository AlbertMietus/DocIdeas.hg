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

Simulation/Verification
=======================

.. use:: Simulate & Verify all possible event-orders
   :ID: U_Tools_EventOrder

   To prevent :ref:`Castle-Heisenbug`, Castle should come with a tools to

   - Simulate “other” event-orders (show it’s effect to the user)
   - Verify that “any” event-order results in a logical & correct result.

   .. seealso:: “:ref:`Dezyne`” has such a tool 

