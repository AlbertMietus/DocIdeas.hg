================
The PEGEN parser
================

.. post:: 2022/10/23
   :category: CastleBlogs, rough
   :tags: Grammar, PEG, DRAFT

   To implement CCastle we need a parser (as part of ther compiler). Eventually, that parser will be writen in Castle;
   but for now we kickstart it in python. Which has several packages that can assist us.  As we like to use an PEG one,
   there are a few options. `Arpeggio <https://textx.github.io/Arpeggio/2.0/>`__ is well known, and has some nice
   options -- but can’t handle `left recursion <https://en.wikipedia.org/wiki/Left_recursion>`__ -- like most
   PEG-parsers.

   Recently python uses a PEG parser, that supports `left recursion <https://en.wikipedia.org/wiki/Left_recursion>`__
   (which is a recent development). That parser is also available as a (hardly documented) package: `pegen
   <https://we-like-parsers.github.io/pegen/index.html>`__

   This blog is writen to remember some leassons learned when playing with in


Build-In Lexer
==============

Pegen is specially writen for Python and use a specialized lexer; unlike most PEG-parser, that uses PEG for both. Pegen
uses the `tokenizer <https://docs.python.org/3/library/tokenize.html>`__ that is part of Python. This comes with some
restrictions.

Tokens
------

The lexer will recognize some tokes that are specialy for python, like `INDENT` & `DEDENT`. Also some generic tokens
like NAME (which is an ID) and `NUMBER` are know, and can be used to define the language.

Unfortunally, it will also find some tokens --typical operators-- that *hardcoded* for python. By we like to use
differently. Possible combined with other characters. Then, those will not be found; not the literal-strings as set in
the grammar.

.. warning::

   .. code-block:: PEG

      Left_arrow_BAD: '<-'	## This is WRONG, as ``<`` is sees as a token
      Left_arrow_OKE: '<' '-'	## This is acceptable

.. seealso:: https://docs.python.org/3/library/token.html
             
.. tip::

   A quick trick to see how a file is split in tokens, use ``python -m tokenize [-e] filename.peg``.
   |BR|
   And make sure you do not use string-literals that (eg) are composed of two tokens.



.. sidebar:: Reserverd Names

   - start
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

