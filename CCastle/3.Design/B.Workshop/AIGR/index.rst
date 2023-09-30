.. _AIGR:

Abstract Intermediate Graph Representation
==========================================

Any Castle program can be translated and represented with an abstract intermediate graph [#graph-tree]_. This
**intermediate language** is used to transfer information between the various parts of the :ref:`Castle-WorkshopTools`.

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :glob:


   *
   */index


---------

.. rubric:: Footnotes

.. [#graph-tree]
   A tree (either `mathematical <https://en.wikipedia.org/wiki/Tree_(graph_theory)>`__ or in `computing
   <https://en.wikipedia.org/wiki/Tree_(data_structure)>`__ is (always) a `graph
   <https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)>`__.  But as soon a tree has an interconnection
   (e.g. when   branches merge), it’s strictly speaking not a tree anymore. Likewise, a collection of trees (sometimes
   called a    *forest*) is not a tree -- as it has no common “root”. But they are all graphs.

   When analysing (Castle) code, it is very similar to a tree: a file has one or more components/classes, which have
   some methods etc. A method is typically defined within one class/component etc. So it’s very tree-alike (and
   the first step of compiling is finding that tree: the AST.

   However, semantically, there are interconnections: the argument of a function call should match the parameters
   of the corresponding function definition, variables defined at one place can be used (or out of scope) at
   another, etc.

   So, to represent and analyse (optimize) a program, we need a graph ...

