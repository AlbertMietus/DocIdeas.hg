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


