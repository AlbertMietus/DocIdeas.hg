.. _rPY:

=============================
rPY: Use (r)Python as backend
=============================


.. post:: 2023/06/25
   :category: Castle, DesignStudy, rough, RPython
   :tags: DRAFT, IDEA, Castle, WorkshopTools,

   When designing a Castle-Compiler with a :ref:`C-backend <CC2Cpy>`, we found some nasty details unrelated to CCastle
   but to the C-language. For example, C has no namespaces (see :ref:`CC2Cpy_NoNameSpaces`); we can simulate them, but
   that is extra work.  Likewise, we need to generate many (data)classes that are very similar. Again, it is
   possible, but it takes a lot of work: to write the code that generates those almost codes.
   |BR|
   Therefore, I started to think about how we can automate that. Or: who has done it before, and what can we borrow?

   `PyPy <https://en.wikipedia.org/wiki/PyPy>`__ --an alternative Python implementation-- has developed a concept for
   that! They have built a translator to convert `(r)Python <https://en.wikipedia.org/wiki/PyPy#RPython>`__ into C and
   compile that into native machine code.
   |BR|
   Can we re-use that? And can it help to realize the “first (bootstrap) compiler” faster?


What is RPython?
================

RPython is a (restricted) subset of Python. Therefore RPython can be executed in any Python compiler/interpreter,
including the typical, standard *CPython* version, or with  PyPy, who invented RPython. They use it to compile their
compiler, as one can translate RPython can into native CPU instructions, also

|BR|
However, RPython is **not** a Python *compiler*! Not all Python code can be translated, only a restricted subset.

RPython is not a tool, either. It's more like a *“sub-language”*, although the PyPy-teams don't describe it like
that. That *language* isn't very strictly defined either: *“When a program can be translated (compiled), it’s
RPython..."* is kind of the rule.

Most relevant is the RPython-toolchain: a (Python) program that will translate a (valid) RPython program into C and
then into CPU instructions.

Why RPython?
-------------

When a Castle-Compiler emits valid RPython, we can translate that into C and then in native instructions. So we can
compile Castle into native instructions!
|BR|
And, when that extra step results in less development work, it sounds like an interesting idea.

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   *

.. seealso::

   * https://rpython.readthedocs.io
   * https://doc.pypy.org/
   * `RPython: Compiling Python to C, for the speed
     <https://maori.geek.nz/rpython-compiling-python-to-c-for-the-speed-5411d57a5316>`__
     [hands-on intro with *Fibonacci in (r)python*]
   * `Converting Python functions to dynamically compiled C
     <https://conference.scipy.org/SciPy2008/static/wiki/ilan_schnell_talk.pdf>`__
     [PDF, also with some code examples]
   * `David Beazley: Tinkering with PyPy & Rpython [video]
     <https://www.youtube.com/watch?v=l_HBRhcgeuQ>`__
     [PDF] *funny & entertaining*!
   * *RPython By Example* (a bit outdated):
     `docs <https://mssun.github.io/rpython-by-example>`__
     &
     `code (git) <https://github.com/mssun/rpython-by-example>`__
   * https://osdn.net/users/albertmietus/pf/TryOut_PyPy-and-Rpython (SLOW!)
     |BR|
     My collection of small rpython demos, and typical Python-code that is not RPython ..

..  LocalWords:  CCastle
..  LocalWords:  RPython CPython
