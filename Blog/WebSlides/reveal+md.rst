===================
Revealjs + Markdown
===================
.. Copyright (C) ALbert Mietus, 2018

.. post::
   :tags: revealjs, md
   :category: WebSlides

`Reveal.js <https://revealjs.com>`_ (`@gitgub <https://github.com/hakimel/reveal.js>`_) is a open-source (MIT-Licensed)
HTML-Framework for easily creating beautiful presentations using HTML. -- According to there website. It has a nice
`live demo <http://revealjs.com>`_ too.

As a cons however, it assumes you speak fluently html, javascript, and are willing to read the code to understand the
features. Or, use the (non open-source) online editor. That does not fit to my wishes ...

However there is an option to use markdown! It comes standard with a plugin to handle several dialects [#dialects]_ of
markdown [#marked]_. Although *md* [#dialects]_ is not *rst*, it is text-based. And so easy to maintain. Apparently, one
can even put in *html-comments* into the *md*-text, to set the features.

Speaking about features: They are hardly documented, but nice. One can specify slide-traditions, animate “fragments”
[#fragments]_, and probably a lot more. So, let try and collect all information!


Concept
=======

We try to stay as close to sphinx as possible. So: *no* html or javascript, except in templates. We allow *MD*, and
where possible we use the syntax that is similar to *rst* [#common]_. Probably we have to allow the html-style
features. And will introduce “next slide” pseudo-directives.

Each “presentation” will consist of 2 files: a html-template [#generate]_ and the *md*-content. Due implementation
details of revealjs, this only works when a web-server is used. A slight drawback, but we can live with it.

Hands-on
========

Paths (installation)
--------------------
After Revealjs is downloaded and installed the html-templates) have to “find” those files. In the examples, the base-url
is shown as ``«revealjs»``. Replace this with the correct directory; often this will be empty, when the are in stalled in
the root-dir of the webserver.

Themes
------

Revealjs has theme-support which is similar to that of (the html-builder of) Sphinx. It mostly comes down to specifying
[#themes]_ a (few) *ccs-file(s)*. That has to be done in the html-template file. For now, we simply hardcoded
one. Search for ``«revealjs»`` in the  examples, and replace by the one you like.

Config
------




Examples
========

.. literalinclude:: democode/html-template-1.html
   :language: html
   :linenos:







----------

.. rubric:: Footnotes

.. [#dialects]	This is still a drawback: `*md*` is hardly a standard language! (unlike `*rst*`)
.. [#marked]	See: https://github.com/markedjs/marked,  https://marked.js.org/
.. [#fragments]	Like: lines, and even words.
.. [#common]	See: https://gist.github.com/dupuy/1855764, and more.
		*Md* has two syntaxes for headers: underlines (``====`` and ``----``) and pound-prefixes (``#`` upto
                ``######``), whereas *rst* uses underlines (in a more flexible way). So we will use underlines in both
                cases.
.. [generate]	Later, this html-file may be generated, possible by a rst-directive. For now it’s a short file one has
                to fill-in by hand.
.. [themes]     Select one of the ones listed in ``«revealjs»/css/theme/``: beige.css black.css blood.css league.css
                moon.css night.css serif.css simple.css sky.css solarized.css white.css, or create a custom one. For
                that, see revealjs docs in https://github.com/hakimel/reveal.js/blob/master/css/theme/README.md
