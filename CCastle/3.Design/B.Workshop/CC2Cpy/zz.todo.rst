TODO (CC2Cpy)
*************

No Name Collisions
==================

.. todo::

   When we generate C code, all names are globals -- *there are no names in C*!
   |BR|
   So, when a file (or package etc) defines a component (or protocol, ect), that happens to have the same name as one in
   another file, they clash. This is known as a *Name Collision*.

   This has to be prevented!

.. tip::

   There are several ways how to circumvent that, like:

   #. Use ‘static’ when possible -- this make the issue smaller, but does not solve it (IMHO)
   #. Use a C++ compiler, that has namespaces -- it’s a workaround -- I don’t prefer that
   #. Prefix all generated names with a **NS-prefix** (*NS::NameSpace*)

      For example ``component Sieve`` should result not in:

      * **struct CC_B_ComponentInterface** ``cc_CI_Sieve``,
      * **struct CC_B_ComponentClass**     ``cc_C_Sieve``, and
      * *typedef struct { ... }*           ``CC_C_Sieve``.

      But in:

      * **struct CC_B_ComponentInterface** ``{NS_hashId}_cc_CI_Sieve``,
      * **struct CC_B_ComponentClass**     ``{NS_hashId}_cc_C_Sieve``, and
      * *typedef struct { ... }*           ``{NS_hashId}_CC_C_Sieve``.

        Where  **{NS_hashId}**, the result of `NS_hashId(dottedNamePath:str)->shortSting` is stable
      
        - python’ hash() will not work
        - See `HashIds <https://hashids.org/python/>`__ for an examle -- but not accepting string-input
        - MD5 is provably fine -- no need to be (crypto) safe

      Or, possible the order should be

      * **struct CC_B_ComponentInterface** ``cc_CI_{NS_hashId}_Sieve``,
      * **struct CC_B_ComponentClass**     ``cc_C_{NS_hashId}_Sieve``, and
      * *typedef struct { ... }*           ``CC_C_{NS_hashId}_Sieve``.




Pre/In/PostFixes in generated CC2Py code
========================================

.. post::
   :category: Castle, DesignStudy, CC2Cpy
   :tags: DRAFT

   The CC2Cpy :ref:`compiler<CC2Cpy>` generated C-code, using a lot of pre-, in- and postfixed.

   They are documented later ..
