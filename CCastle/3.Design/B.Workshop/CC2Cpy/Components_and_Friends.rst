=========================================
Modeling & Rendering Components & Friends
=========================================

.. post::
   :category: Castle, DesignStudy, CC2Cpy
   :tags: DRAFT

   Any compiler will read & parse the source, convert it into an abstract natation (like the AST) and write the result
   back in a lower-language, or “binary format”. We have spend several posts on the parsing phase. This one focus on
   the last part: *rendering* the model into “generated C code”.

   The goal is not to design “all & everything”. We pick some details, do some experiment (typically in Jupyter/IPython
   Notebook), and the lessons-learned are documented here.


.. IPython Sources

  * ModelMore.ipynb, which is based on
  * Model-GCD.ipynb

  They have become outdated by this (draft) post

.. todo::

   * Add (pseudo) namespaces-support, global/extern/static keyword and such (during generation)
   * Better design & describe the Pre/In/PostFixes (see XXXX)

Overview
=========

Each component has 3 structures to fully describe the component; most are generated and/or filled by the compiler.

**CC_B_ComponentInterface**
   Describes the interface of a Component; more or less as by the Moat file
**CC_B_ComponentClass**
   A *directory* of the component implementation: which callables etc -- including a “dispatch (v)table”
*CC_C_${CompName}*
   Data-structure for each instance for component *${CompName}* -- the place to store component-local-data

* The first two are predefined (build-in) structures, that are filled (and named) by the compiler. (so global variables)
* The last one is defined (``#typedef``) by the compiler.
  |BR|
  This is handled by :class:`CC_Component`

For each component that is *coded* in a Castle file, the CCastleCompiler will fill the structures :c:struct:`CC_B_ComponentInterface` and a :c:struct:`CC_B_ComponentClass`. Or more exact, it generates C-code to create a “global, read-only” variable (that will end up in de data-segment). This is part of the runtime.
|BR|
Those variables get names as ``cc_CI_${CompName}`` resp ``cc_C_${CompName}`` (notice the lowercase prefix)

The CCastleCompiler will also define a *new* structure (as a typedef), called ``CC_C_${CompName}`` (notice the uppercase prefix). They are not instantiated by the compiler. During executing of the Castle program, such a structure will be allocated for each component-instance. The size of the structure depend on the component. And as component do inherit, the structure-fiels of all super-components tripple down in the (top of) the new structure!  This implies all ``CC_C_${CompName}`` structures start by ("inherite from") the baseComponent -- which struct is called c:type:`CC_B_Component` -- Notice the **B** in the name.

.. Note::

   * The names of the structures & variables are based on the *"handCompiled"* version; they can/will change. But need to be aligned.
   * The variables ("instances") start with **cc_**; in small-case. 
   * The structures ("classes") start in **CC_**; in capital. 
   * Therefore, *cc_C_${CompName}* and *CC_C_${CompName}* are not the same.
     |BR|
     The first is a instance of a CC_B_ComponentClass, the second is a generated type (for the same component
   * This can be a bit confusing. Probably I will change the name(s) once ...

.. hint:: Pre/In/Post-fixes

   * Components

     - **_CI_** (infix) stands for **C**\omponent-**I**\nterface,
     - **_C_**  (infix)     stands for **C**\omponent (implementation).
     - *Probably beter abrivations will help*

   * **_B_** (infix) stands for **B**\uildin
   * **CC_** (prefix) is alike CCaste


