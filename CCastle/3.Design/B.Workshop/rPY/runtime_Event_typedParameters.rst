.. include:: /std/QuickNote-tip.irst

====================================
QuickNote: typedParameters in Event?
====================================

.. post:: 2023/10/2
   :category: RPy, rough, QuickNote
   :tags: Castle, WorkshopTools, DesignStudy

   The RPy compiler backend needs to *‘fill-in’* some data structures, like ``CC_B_Protocol`` -- there is one for every
   protocol. It contains the name of the protocol, its *kind* (like `Event`, as we assume here), and a list of
   **events**. That event list contains the (event) name, it’s sequence-number (see: :ref:`EventIndex`), and a backlink
   to the protocol.

   **The question is**: Should the ``Event`` (dataclass) contain the typedParameters?

   This question affects both the runtime (for this backend) --the RPython implementation of
   ``CC.buildin.CC_B_P_EventID``-- and the (:ref:`jinja templating <rPY-Jinja>`) to generate the code to fill those
   data-structures.

Intro
======

When implementing (and testing) the :ref:`RPy backend <rPY>`, I discovered the use of TypedParameters was not
consistent. In some :ref:`Jinja templates <rPY-Jinja>` that information was written into (generated) RPython files, in
others not. Also, as was sometimes required by the “reference” files, and in other case not.

Because those (generated) files can’t be run (before all/most of the files can be written), that mistake was only
discovered recently [#noCC]_.

So, I have to make a “Design Decision”: put those TypedParameters always in the generated code, or newer?

TypedParameters?
----------------

As a reminder:

* The **parameters** `or (formal arguments) <https://en.wikipedia.org/wiki/Parameter_(computer_programming)>`__ are the
  “placeholders” in the function definition; they always have a name (that is used as a variable in the body), and
  optionally a type -- this depends on the language. In Castle, parameters have types
  |BR|
  When calling those functions, we speak about arguments; then they have a value.

* We use the term **TypedParameters** to denote a sequence (a list/array) of TypedParameter (`S`); where each
  TypedParameter is a tuple of a `name` and a `type`.

Why (Not)
==========

When a Castle program defines (e.g.) an event, the *parameters* are given. The Castle-compiler should check the
remainder of the program for consistency [#errorcheck]_ and so, TypedParameters are used at many places [#AIGR]_.
|BR|
That is however another matter.

Here the question is; should that information be “stored” inside the (generated) code, so that the program itself can
inspect it [#introspection]_? -- that is runtime ...

Doubtless, we can write code without this feature; ‘`:ref:`Castle-TheSieve`’ does not need it.
But, unequivocally, when it is available -- like in Python, it is a powerful feature. The question however is: what does
it do in Castle?
|BR|
That is a hard question.

Other languages
---------------

When studying other languages, we see several approaches. Older, traditional languages (like C and the early
versions of C++) do not have it. Modern languages, like Python, do use it heavily (although some claim: “do misuse it”).

C (ansi C)
~~~~~~~~~~

Not an option

C++
~~~~

C++, as an “OO version of C”, traditionally did not support any form of runtime information.

Recent versions of C++ have a limited version of it; even in two approaches:
- (type) traits: https://en.wikipedia.org/wiki/Trait_(computer_programming)
-  RTTI: https://en.wikipedia.org/wiki/Run-time_type_information`

C#
~~~

C-sharp supports something called introspection or reflection. There is a lot of online discussion whether it is a
fully-flagged feature, or just changing names. I’m not going to judge here.
|BR|
Apparently, the feature is useful -- if it is not, nobody would care to discuss it.


Java
~~~~

Java has something called  `The Reflection API <https://docs.oracle.com/javase/tutorial/reflect/index.html>`_ (although
it says one should use “improvements” -- without any links.)

Python
~~~~~~

Everything in Python is an object, that holds “life type information” (including doc-strings, type and even code). One
can runtime inspect types (and names), and even generate new types. Can be very convenient.

Ruby
~~~~

Roughly the same as in Python, see above.

Rust
~~~~

After a bit of googling, it appears that Rust does not have any (powerful) feature to inspect types at runtime --
although it has something called “traits”. Still, the sources on the internet are not clear about it -- some say it
has, some say certainly it has not.
|BR|
Given no text-books write about when or how to use it, I assume it’s not available.


Design Decision
===============

Given, many languages like it, we made some decisions; both for the long run, and for the short one.

.. use:: Introspection is an option
   :ID: U_Introspection

   At the moment, we see no reason to have the TypedParameter info available in the runtime. The current (Castle)
   examples do not use it, nor is that info used in the “handCompiled” code (incl :ref:`Sieve_in_rPython`).

   On the other-hand, it is very powerful (e.g. in Python), and “bolted-on” to a traditional language such as C++ with
   `(type) traits <https://en.wikipedia.org/wiki/Trait_(computer_programming)>`__.

   Therefore, we like to keep it as an option, for future addition. This implies we have to design the interface in the
   language.

.. resolution:: No TypedParameter is 1st compiler
   :ID: DD_No_Introspection_in_1st
   :links: U_Introspection, U_Introspection_API

   The first (bootstrap) compilers don’t need to support introspection.

   And so, the (initial) RPy backend does not have to store TypedParameters (for events) in the runtime.
   |BR|
   Likewise, the language (design) doesn't have to embrace this.

.. use:: Introspection interface
   :ID: U_Introspection_API

   Eventually, the Castle language should support introspection. (but now now, see :need:`DD_No_Introspection_in_1st`).

   This implies we have to make a great language design on the interface (for the Castle programmer) on how to use
   it. We like that is act as a “1ste class citizen”, not as a “bolt-on addition”

------------


.. rubric:: notes

.. [#noCC]
   Recall, the generated files “fill-in” some dataclass, that are part of the :file:``CC/buildin`` library, which isn’t
   developed yet. Only the ref:`Sieve_in_rPython` (as well as the *handCompiledC* C-version) versions are used reference.
   
.. [#errorcheck]
   By example, the (Castle) compiler should give a error when a programmer makes mistake in (e.g.) the order or number
   of parameters, or in the typing, or ...

.. [#AIGR]
   As the information is needed internally in the compiler, the :ref:`AIGR <AIGR>` contains it.

.. [#introspection]
   This features is often called *introspection*, and for a language as Python it is really important. Other languages, as C
   and C++ do not have it. Or very limited.
   |BR|
