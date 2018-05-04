.. _revealmd:

===================
Revealjs + Markdown
===================
.. Copyright (C) ALbert Mietus, 2018

.. post:: 2018/04/28
   :tags: revealjs, md
   :category: WebSlides

   `Reveal.js <https://revealjs.com>`_ (`@gitgub <https://github.com/hakimel/reveal.js>`_) is a open-source
   (MIT-Licensed) HTML-Framework for easily creating beautiful presentations using HTML ---according to there
   website. It has a nice `live demo <http://revealjs.com>`_ too.

   I’m going to use it with markdown however...

Revealjs and its documentation assumes you speak fluently html, javascript, and are willing to read the code to
understand the features. Or, use the (non open-source) online editor. That does not fit to my wishes ...

However there is an option to use *markdown*! It comes standard with a plugin to handle several dialects [#dialects]_ of
markdown [#marked]_. And although *md* [#dialects]_ is not *rst*, it is text-based. And so easy to maintain. Apparently,
one can even put in *html-comments* into the *md*-text, to set the “features”.

Speaking about features: They are hardly documented, but nice. One can specify slide-traditions, animate “fragments”
[#fragments]_, and probably a lot more. So, let try and collect all information!


Concept
=======

We try to stay as close to sphinx as possible. So: **no** html nor javascript, except in templates. We allow *md*, and
where possible we use the syntax that is similar to *rst* [#common]_. Probably we have to allow the html-style
features. And we will introduce “next slide” pseudo-directives.

Each “presentation” will consist of 2 files: a :ref:`html-template <html-template>` [#generate]_ and the
:ref:`md-content <md-content>`. Due implementation details of revealjs, this only works when a web-server is used. A
slight drawback, but we can live with it.

.. todo:: demo

----------

.. rubric:: Footnotes

.. [#dialects]	This is still a drawback: *md* is hardly a standard language! (unlike *rst*)
.. [#marked]	See: https://github.com/markedjs/marked,  https://marked.js.org/
.. [#fragments]	Like: lines, and even words.
.. [#common]	See: https://gist.github.com/dupuy/1855764, and more.
		*Md* has two syntaxes for headers: underlines (``====`` and ``----``) and pound-prefixes (``#`` up-to
                ``######``), whereas *rst* uses underlines (in a more flexible way). We will use underlines in both
                cases.
.. [#generate]	Later, this html-file may be generated, possible by a rst-directive. For now it’s a short file one has
                to fill-in by hand.
