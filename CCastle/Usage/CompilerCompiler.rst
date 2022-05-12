.. _Castle-CompilerCompiler:

=================
Compiler Compiler
=================

.. post:: 2022/05/13
   :category: Castle, rough
   :tags: Castle

   In Castle you can define a *grammar* directly in your code. The compiler will *translate* them into functions, using
   the build-in (PEG) **compiler-compiler** -- at least that was it called back in the days of *YACC*.

   How do one use that? And why should you?

Grammars, a short intro
=======================

A grammar is a collection of (parsing)-**rules** and optionally some *settings*.  Rules are written in a mixture of EBNF
and PEG meta-syntax.  Let’s start with an simple example::

  castle_file  <- ( import_line | interface | implementation )* ;
  import_line  <- IMPORT_stmt ( STRING_literal | qualID ) ';' ;
  qualID       <-  '.'? nameID  ('.' nameID )*   ;
  IMPORT_stmt  =   "import" ;
  ...

This basically defines that a ``castle_file`` is either an ``import_line``, an ``interface``, an ``implementation``, or
sequence of them. Where an ``import_line`` (or statement) starts with ``IMPORT_stmt`` *(which is set to the string
‘import’, on line 4)*, then has either a ``STRING_literal`` (indeed a literal-string) or a ``qualID``, and ends with a
semicolon (`;`). Likewise, a ``qualID`` is a ``nameID`` *(a name that is used as ID, like in any programming language)*,
optionally followed by sub-names *(again like most languages: a dotted name, specifying a field (in a field, in ...) a
variable*. In Castle, that name may start with a dot --which is a shorthand notation for “in the current namespace. You
can ignore that for know.

The grammer defines how one should read the input --a text--, or more formally how to parse it. The result of this
parsing is twofold. It will check whether input conforms to the grammer; resulting a in boolean, for the mathematics
under us. And is will translate a sequential (flat) text into a tree-structure; which typically much more useful for a
software-engineer.
|BR|
A well known example is this HTML-file. On disk it’s nothing but text, which are easy to store, and to transfer. But
when send to your brouwer, they are *parsed* and create the `DOM
<https://nl.wikipedia.org/wiki/Document_Object_Model>`__; a tree of document(s), paragraphs, tables with rows and cells,
etc.

Parsing
=======
Another well-known example is (the source of a) programm. As code, it is just text. But the compiler will parse it into
a parse-tree and/or an abstract-syntax-tree; which is build out of classes, methods, statements etc.
|BR|
But also your favorite IDE will *parse* it; to highlight the code, give tooltips, enable you to quickly navigate and
refactor it, and all those conviant features that make it your favorite editor.

And even you are probably parsing text as part of your daily job. When you un-serialise data, you are (often) parsing
text; when you read the configuration, you are (or should be ) parsing that text. Even a simple input of the user might
need a bit of parsing. The text “42”  is not the number :math:`42.0` -- you need to convert it; parse it.

There a many ways to *parse*. You do not need a full-fledged grammer to translate “42” into :math:`42` or
:math:`42.0` --a stdlib functions as ``atoi()`` or ``atof()``  will do. But how about handling complex numbers
(:math:`4+j2`), fractions (:math:`\frac{17}{42}`)?

Non-parsing
-----------

As proper passing used to hard, other similar (but simpler) techniques do exist, like `globing
<https://en.wikipedia.org/wiki/Glob_(programming)>`__ (\*.Castle on the bash-prompt will result in all
Castle-files). Using `regular-expressions <https://en.wikipedia.org/wiki/Regular_expression>`__ is more powerfull, and
other used to highlight code; a pattern as `//.*$` can be used to highlight (single-line) comment. It often works, but
this simple pattern might match a piece of text *inside* a multi-line-(doc)string -- which wrong.

Grammars are more powerfull
===========================

A grammar (even a simple one) is more powerfull. You can define the overal structure of the input and the sub-structure
of each *lump*. When a multi-line-string has no sub-structure, the parser will never find comments inside it. Nor other
way around; it simple is not hunting for it.

As most programming-languages do not have build-in support for grammars, one has to resort to external tools. Like the
famous `YACC <https://en.wikipedia.org/wiki/Yacc>`__; developed in 197X. YACC will read a grammar-file, and generates
C-code that can be compiled and linked to your code.

Back then, writing compiler-compilers was a popular academic research exercise (YACC stand for: Yet Another Compiler
Compiler). It was great for compiler-designers, but clumsy to use for average developers: The syntax to write a grammar
was hard to grasp, with many pitfalls, the interface between your code and the parser was awkward (you had to call
``yyparse()``; needed some globals; OO wasn't invented, no inheritance or data-hiding, which resulted in puzzling tricks
to use multiple parsers, etc).
|BR|
Aside of that, more and better parsing strategies are developed; that is handles in another :ref:`blog <grammmar-code>`.

Unleash that power
------------------

With those better algorithms, faster computers having a lot more memory available, and other inventions writing grammar
has become more peaceful. Except that you still need an extra step, another sytax, as you still need to use an external
tool. That sometimes isn’t maintained after a couple of years ...
|BR|
The effect is, most developers don’t use it. The write parser-like code manually, the settle for less optimal result. Or
are utterly not aware that grammer can provide a other (better, easier) solution.

As castle has build-in support for grammers and is hiding you from the nasty details of parsing-strategies, how to
generating code first, then compile it, and use (call it) at the same time.
|BR|
With a few lines, you define the structure of the input. Each rule has a name (the left-hand-side of the rule. so the
part before the arrow).


To use the grammar, you simple use those names as functions: call them with a input (string), and it will return a
(generic) tree-structure.
|BR|
When you simple like to verify the syntax is correct: use the tree as a boolean: when it not-empty the input is valid.

But typically you proces/use that tree: like you do in many situations. Read the configuration values, walk over the
tree, of traverse it as-iff it is a DOM. You can even use Castle’s :ref:`matching-statements` to simply that.

