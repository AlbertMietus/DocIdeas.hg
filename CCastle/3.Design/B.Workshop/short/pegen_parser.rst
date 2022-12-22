.. include:: /std/localtoc.irst

.. _QN_PEGEN:

================
QuickNote: PEGEN
================

.. post:: 2022/11/3
   :category: CastleBlogs, rough
   :tags: Grammar, PEG

   To implement CCastle we need a parser, as part of the compiler. Eventually, that parser will be written in Castle. For
   now, we kickstart it in python; which has several packages that can assist us.  As we like to use a PEG one, there
   are a few options. `Arpeggio <https://textx.github.io/Arpeggio/2.0/>`__ is well known, and has some nice options --
   but can’t handle `left recursion <https://en.wikipedia.org/wiki/Left_recursion>`__ -- like most PEG-parsers.

   Recently python itself uses a PEG parser, that supports `left recursion
   <https://en.wikipedia.org/wiki/Left_recursion>`__ (which is a recent development). That parser is also available as a
   package: `pegen <https://we-like-parsers.github.io/pegen/index.html>`__; but hardly documented.

This blog is written to remember some lessons learned when playing with it. And as kind of informal docs.

.. seealso:: :ref:`QN_Arpeggio` is another candidate package for the PEG parser in the initial :ref:`Castle-WorkshopTools`

Build-In Lexer
==============

Pegen is specially written for Python and uses a specialised lexer; unlike most PEG-parser that uses PEG for lexing too. Pegen
uses the `tokenizer <https://docs.python.org/3/library/tokenize.html>`__ that is part of Python. This comes with some
restrictions.

This lexer -or tokenize(r) as python calls it-- is used **both** to read the grammar (the PEG file) *and* to read the
source-files that are parsed by the generated parser.

.. hint::

   These restrictions apply when we use pegen as module: ``pyton -m pegen ...``; that calls `simple_parser_main()`.
   |BR|
   But also when we use the parser-class in own code --so, when importing pegen ``from pegen.parser Parser ...``-- it is
   restricted.  Then is a bit more possible, as we can configure another (self made) lexer. The interface is quite narrow
   to python however.


Tokens
------

The lexer will recognise some tokes that are special for python, like `INDENT` & `DEDENT`. Also some generic tokens
like NAME (which is an ID) and `NUMBER` are know, and can be used to define the language.

Unfortunately, it will also find some tokens --typical operators-- that *hardcoded* for python. Even when we like to use
them differently; possible combined with other characters. Then, those will not be found; not the literal-strings as set
in the grammar.

.. note::

   Pegen speaks about *(soft)* **keywords** for all kind of literal terminals; even when they are more like operators
   than *words*.

.. warning::

   When the grammar defines (literal) terminals (or keywords) --especially for operators-- make sure the lexer will not
   break them into predefined tokens!
   |BR|
   This will not give an error, but it does not work!

   .. code-block:: PEG

      Left_arrow_BAD: '<-'	## This is WRONG, as ``<`` is seen as a token. And so,  `<-` is never found
      Left_arrow_OKE: '<' '-'	## This is acceptable

   This *splitting* results however in 2 entries in the resulting tree --unless one uses `grammar actions
   <https://we-like-parsers.github.io/pegen/grammar.html#grammar-actions>`__ to create one new “token”.

.. seealso:: See https://docs.python.org/3/library/token.html, for an overview of the predefined tokens

.. tip::

   A quick trick to see how a file is split into tokens, use ``python -m tokenize [-e] filename.peg``.
   |BR|
   Make sure you do not use string-literals that (eg) are composed of two tokens. Like the above mentioned ``<--``



.. sidebar:: Reserved
   :class: localtoc

   - showpeek
   - name
   - number
   - string
   - op
   - type_comment
   - soft_keyword
   - expect
   - expect_forced
   - positive_lookahead
   - negative_lookahead
   - make_syntax_error

Rule names
----------

The *GeneratedParser* inherits and calls the base ``pegen.parser.Parser`` class and has methods for all
rule-names. This implies some names should not be used as rule-names (in all cases) -- see the sidebar.


Meta Syntax (issues)
====================

No: regexps
-----------

PEGEN has **no** support for regular expressions probably as it uses a custom lexer.

Unordered Group starts a comment
--------------------------------

PEGEN (or it lexer) used the ``#`` to start a comment.  This implies an **Unordered group** ``( sequence )#`` --as in
`Arpeggio <https://textx.github.io/Arpeggio/2.0/grammars/#grammars-written-in-peg-notations>`__-- are not recognized

A workaround is to use another character like ``@`` instead of the hash (``#``).


Result/Output
=============

cmd-tool
--------

The command-line tool  ``pyton -m pegen ...`` only prints the parsed tree: a list (shown as ``[`` ... ``]``) with
sub-list and/or `TokenInfo` named-tuples. Each `TokenInfo` has 5 elements: a token type (an int and its enum-name), the
token-string (that was was parsed), the begin & end location (line- & column-number), and the full line that is being
parsed.

No info about the matched gramer-rule (e.g. the  rule-name) is shown. Actually that info is not part of the parsed-tree.

.. seealso:: This `structure is described <https://docs.python.org/3/library/tokenize.html?highlight=TokenInfo>`__ in
             the tokenize module; without specifying its name: TokenInfo.

The parser
----------

The GeneratedParser (and/or it’s baseclass: ``pegen.parser.Parser``) returns only (list of) tokens from the tokenizer (a
OO wrapper around tokenize). And so, the same TokenInfo objects as described above.

Stability
=========

The current pegen package op `pypi <https://pypi.org/project/pegen/>`__ is V0.1.0 -- which already shows it not
mature.  `That version github <https://github.com/we-like-parsers/pegen/tree/v0.1.0>`__ is dated September 2021 (with 36
commits). The `current <https://github.com/we-like-parsers/pegen/tree/db7552dda0af6b27cbbb1230be116e8a56c49736>`__
version (Nov 22) has 20 commits more (56).
|BR|
And can be installed with ``pip install git+https://github.com/we-like-parsers/pegen``

It os however, not fully compatible. By example ``pegen/parser.y::simple_parser_main()`` now expect an ATS object (to
print), not a list of TokenInfo.

.. tip::

   The pegen package is **NOT** used inside the `(C)Python tool
   <https://github.com/python/cpython/tree/main/Tools/peg_generator>`__; the CPython version is heavily related to other
   details of CPython; it can also generate C-code. The pegen-package is based on it, and more-or-less in sync, can
   generate Python-code only, but is not depending on the compiler-implementation details.

   .. seealso::  https://we-like-parsers.github.io/pegen/#differences-with-cpythons-pegen


Buggy current version
---------------------

The git version contains (at least) one bug. The function ``parser::simple_parser_main()``, that is called when using the
generated file, uses the AST module to print (show) the result -- which simple does not work.
|BR|
Probably, that* default main* isn’t used a lot (Also, I prever to use -- have use-- a own main). Still it shows it
immaturity.


..  LocalWords:  lexer tokenize cpython regexps tokenizer
