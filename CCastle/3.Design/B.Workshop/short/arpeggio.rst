.. _QN_Arpeggio:

===================
QuickNote: Arpeggio
===================

.. post:: 2022/11/8
   :category: CastleBlogs, rough
   :tags: Grammar, PEG

   In this short QuickNote, we give a bit of info on `Arpeggio <https://textx.github.io/Arpeggio/2.0/>`__; a python
   package to implement a (PEG) parser. Eventually, the parser is written in Castle -- like all
   :ref:`Castle-WorkshopTools`. To kickstart, we use python and python-packages. Where arpeggio is one of the options.

   As Arpeggio is quite well `documented <https://textx.github.io/Arpeggio/2.0/>`__ this is a short note. We also describe
   some differences with the :ref:`Pegen <QN_PEGEN>` package.

.. seealso:: :ref:`QN_PEGEN` another candidate package for the PEG parser in the initial :ref:`Castle-WorkshopTools`

TextX & Arpeggio
================

Arpeggio is part of `TextX <http://textx.github.io/textX>`__, a python clone of (the java-based) XText --a language
workbench for building DSLs.  `Arpeggio <https://textx.github.io/Arpeggio>`__ is the PEG parser for those
Domain-Specific Languages.

Arpeggio takes another route than most parsers. It does not need a (text file) grammar to generate a parser for it, one
can configure the grammar with python statements and directly use it -- no generation is needed. Alternatively, one can
read a text-based grammar-- multiple meta-grammars are supported-- that is parsed first to configure the requested
parser.
|BR|
This can be a bit confusing, at first sight; but is quite convenient. It also shows the power of both Python and
Arpeggio itself. After all, Arpeggio is a parser to read any language; even a meta-language that describes the
languages.

Parse-Tree
----------

After creating the grammar in `python <https://textx.github.io/Arpeggio/2.0/grammars/#grammars-written-in-python>`__ or
a `PEG meta-grammar <https://textx.github.io/Arpeggio/2.0/grammars/#grammars-written-in-peg-notations>`__ one can run
the parser to parse a source file.

The result is a Parse-Tree, where each leave is a terminal node: a StrMatch or a RegExMatch object. All other nodes
(non-terminals) are created by the grammar. Each node has a ``.name`` attribute: the parsing expression (name) that
created it. It has some other convenient attributes too, like the references to the location in the source file.

.. hint:: This feature -- named nodes-- is missing in the :ref:`Pegen <QN_PEGEN>` parsers.


Visitors
--------

Arpeggio has no inline actions [#Meta-Actions]_ (ref: :ref:`GrammarActions`). Instead, a visitor pattern can be used. For
each node (kind) in the parse-tree, a visitor :code:`visit_{node}(self, node, children)` can be written. Or, should be
written -- as the default is to return a ``SemanticActionResults`` instance; which is often quite useless.

.. note::

   Arpeggio call phase `Semantic analysis <https://textx.github.io/Arpeggio/2.0/semantics/>`__; which can be a bit
   misleading as it generally is used to build the AST. Which is the input for the semantic-analyse, in a future step.

Mata-Syntax
===========

Arpeggio supports the normal PEG semantics, including the lexer (aka tokenizer). Tokens can be described by literal
strings, or by regular expressions -- the latter is very powerful.


----------------------------

.. rubric:: Footnotes

.. [#Meta-Actions]
   As Arpeggio is very flexible in its input grammar, it would be possible to add a PEG-Grammar that includes inline
   actions. That, however, is out of scope.

..  LocalWords:  XText lexer tokenizer
