====================
CCastle Design Notes
====================

Castle has to be designed. Not only the “compiler”, but also the language itself. And the **“CC” concept**, And ....

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   *
   */index


.. note:: In case you are wondering: *“Are FSMs and Grammars related, or the same?”*

   The are related, but not equal. As discovered by `Chomsky <https://en.wikipedia.org/wiki/Noam_Chomsky>`__ there is a
   `hierarchy <https://en.wikipedia.org/wiki/Chomsky_hierarchy>`__ of languages (or actually grammars).  As Chomsky was
   studying all kind of languages, include natural “human” language, his perception differs from our interpretation.
   |BR|
   When we (SW/Engineers) speak about grammars, we typically refer to “Context free grammars” (`CFG
   <https://en.wikipedia.org/wiki/Context-free_grammar>`__) -- Chomsky classify them as “Type-2”.

   A non-deterministic Push~Down machine (`PDA <https://en.wikipedia.org/wiki/Pushdown_automaton>`__) is needed to
   recognise a “Type-2” (CFG) Grammar. (Which is a simple version of a stack-machine, which is lot more restricted then a Turing Machine).
   |BR|
   And as a FSM is one of the most restricted machines that exist --it can recognise only “Type-3” `Regular grammar
   <https://en.wikipedia.org/wiki/Regular_grammar>`__-- a FSM can’t be used to recognise a (CFG) grammar.

   .. seealso::

      .. postlist::
         :category: Castle
         :tags: FSM

      .. postlist::
         :category: Castle
         :tags:  Grammar
