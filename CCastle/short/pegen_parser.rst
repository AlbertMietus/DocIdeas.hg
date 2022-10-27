.. include:: /std/localtoc.irst

================
QuickNote: PEGEN
================

.. post:: 2022/10/27
   :category: CastleBlogs, rough
   :tags: Grammar, PEG, DRAFT

   To implement CCastle we need a parser; as part of the compiler. Eventually, that parser will be writen in Castle. For
   now we kickstart it in python; which has several packages that can assist us.  As we like to use an PEG one, there
   are a few options. `Arpeggio <https://textx.github.io/Arpeggio/2.0/>`__ is well known, and has some nice options --
   but can’t handle `left recursion <https://en.wikipedia.org/wiki/Left_recursion>`__ -- like most PEG-parsers.

   Recently python itself uses a PEG parser, that supports `left recursion
   <https://en.wikipedia.org/wiki/Left_recursion>`__ (which is a recent development). That parser is also available as a
   package: `pegen <https://we-like-parsers.github.io/pegen/index.html>`__; but hardly documented.

   This blog is writen to remember some leassons learned when playing with it. And as kind of informal docs.


Build-In Lexer
==============

Pegen is specially writen for Python and use a specialized lexer; unlike most PEG-parser that uses PEG for lexing too. Pegen
uses the `tokenizer <https://docs.python.org/3/library/tokenize.html>`__ that is part of Python. This comes with some
restrictions.

.. hint::

   This applies mostly when we use pegen as modele: ``pyton -m pegen ...``; that calls `simple_parser_main()`.
   |BR|
   When uses it in code, by importing pegen ``from pegen.parser Parser ...`` one has more options (not studies yet).


Tokens
------

The lexer will recognize some tokes that are specialy for python, like `INDENT` & `DEDENT`. Also some generic tokens
like NAME (which is an ID) and `NUMBER` are know, and can be used to define the language.

Unfortunally, it will also find some tokens --typical operators-- that *hardcoded* for python. Even when we like to use
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

.. seealso:: See https://docs.python.org/3/library/token.html, for an overiew of the predefined tokens

.. tip::

   A quick trick to see how a file is split into tokens, use ``python -m tokenize [-e] filename.peg``.
   |BR|
   Make sure you do not use string-literals that (eg) are composed of two tokens. Like the above mentioned ``<--``



.. sidebar:: Reserverd
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

The *GeneratedParser* inherites and calls the base ``pegen.parser.Parser`` class and has methods for all
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

A workarond is to use another character like ``@`` instead of the hash (``#``).


Result/Output
=============

cmd-tool
--------

The commandline tool  ``pyton -m pegen ...`` only prints the parsed tree: a list (shown as ``[`` ... ``]``) with
sub-list and/or `TokenInfo` namedtuples. Each `TokenInfo` has 5 elements: a token type (an int and its enum-name), the
token-string (that was was parsed), the begin & end location (line- & column-number), and the full line that is beeing
parsed.

No info about the matched gramer-rule (e.g. the  rule-name) is shown. Actually that info is not part of the parsed-tree.

.. seealso:: This `structure is described <https://docs.python.org/3/library/tokenize.html?highlight=TokenInfo>`__ in
             the tokenize module; without specifying its name: TokenInfo.

The parser
----------

The GeneratedParser (and/or it’s baseclass: ``pegen.parser.Parser``) returns only (list of) tokens from the tokenizer (a
OO wrapper arround tokenize). And so, the same TokenInfo objects as described above.
