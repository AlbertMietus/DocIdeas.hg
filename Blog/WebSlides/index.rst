WebSlides
=========
.. Copyright (C) ALbert Mietus, 2018

.. post:: 2018/4/27
   :category: WebSlides

   `Sphinx <http:\\Sphinx-doc.org>`_ and `reStructuredText (RST) <http://docutils.sourceforge.net/rst.html>`_ are great
   tools to build *and maintain* documentation. However, the ability for “slide decks” is limited. In practice, most of
   my presentation are made by `PowerPoint` or `Keynote` -- and so, are hard to maintain.

   This has to be changed ..

Out of the box, there are several options, both with and without Sphinx. `Hieroglyph <http://docs.hieroglyph.io>`_ by
example, adds a *builder* to Sphinx, for HTML-based presentation. Whereas `reveal.js <https://revealjs.com>`_ uses
(simplified) html with a javascript-library which is used.  Html isn’t the simplest way to author (& maintain) slides;
there are many attempts to generate revealjs from RST, MD (etc). And revealjs has even a option to use markdown.

In this chapter, several articles (or blogs: :ref:`category-webslides`) give an overview on
existing options. And describe my search to combination to a useful combination.

.. toctree::

   reveal+md
   html-template
   md-content
   design-options

