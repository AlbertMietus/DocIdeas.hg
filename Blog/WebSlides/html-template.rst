.. _html-template:

=================
The html-template
=================
.. Copyright (C) ALbert Mietus, 2018

.. post:: 2018/04/28
   :tags: revealjs
   :category: WebSlides

   Within the concept as described in :ref:`revealmd`, a “html-template” is needed.

   Although such a file is needed for each webslide, most of this html-template is “fixed”. Typically a standard one is
   composed once, and that one is configured per webslide. Both steps are described in this article.

Configure the html-template
===========================

Only two or three items should be configured for each webslide. In the examples, the notation ``〖...〗`` is used for
items that should be set for webslide.
All text, including those braces itself should be set for each webslide.

Title
-----

The title of the presentation (used in the window or tab) is set by the ``<title>`` tag in the html-template.

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 3
   :lineno-match:

Md-file
-------

To chain the html-template and the md-file, the later has to be configured in the first (which is loaded in the
browser). We have chosen to give the two files the same base-name (and differ the extension: `.html` vs `.md`)

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 10
   :lineno-match:

Theme
-----

Revealjs has theme-support which is similar to that of (the html-builder of) Sphinx. It mostly comes down to specifying
[#themes]_ a  *ccs-file*. That has to be done in the html-template file. For now, we simply hardcoded
one. Search for ``«theme»`` in the  examples, and replace by the one you like.

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 5
   :lineno-match:

.. note:: Compose or Configure?

   Typically, I use the same theme for multiple webslides. Therefore, I “compose” a (or a few) basic html-template(s),
   and don’t “configure” them later. Others may configure it for each webslide.

   This also applies to :ref:`global-design`, some may configure those line pro webslide.

Compose the html-template
=========================

In the examples the notation ``«...»`` is used for all items that normally are normally set only once.


Path
----

After Revealjs is downloaded and installed, the html-templates have to “find” those files. In the examples, the base-url
is shown as ``«revealjs»``. Replace this with the correct directory; often this will be empty, when the are in stalled in
the root-dir of the webserver.

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 4-5
   :lineno-match:

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 19-22
   :lineno-match:

Slide-separators
----------------

As *md* has **no** *slide concept* ( nor “page”), an regexp has to be defined to denote the nextslide
[#sections]_. Besides, revealjs has slides at *multiple level*: typical horizontal and vertical ones.

The following pseudo-directives are defined. Multiple spaces around the directive-word are allowed. Parameters after the
pseudo-directive are allowed too, but ignored! No options (``:keyword:``-lines) are possible.

``.. nextslide::``
     This denotes a new (horizontal) slide. The *next* part is optional (allowing ``.. slide::``)

``.. subslide::``
     This starts a (new) “vertical” slide. As an alternative ``.. vlside::`` is allowed also.

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 11-12
   :lineno-match:

.. _global-design:

Global design
-------------

Both revealjs, and its plugins, have a great number of options, that define the “look & feel of the presentation. Most
default values are quite useful. My standard template change a few ones. See below.

Most design options can be set per slide (or fragment) also; see :ref:`design-options` for an overview.

.. literalinclude:: democode/html-template-1.html
   :language: html
   :lines: 23-28
   :lineno-match:

The complete file
=================

.. literalinclude:: democode/html-template-1.html
   :language: html
   :linenos:
   :emphasize-lines: 3, 4-5, 19-22, 10, 11-13, 23-28



----------

.. rubric:: Footnotes



.. [#themes]	Select one of the ones listed in ``«revealjs»/css/theme/``: beige.css black.css blood.css league.css
                moon.css night.css serif.css simple.css sky.css solarized.css white.css, or create a custom one. For
                that, see revealjs docs in https://github.com/hakimel/reveal.js/blob/master/css/theme/README.md
.. [#sections]	An often used alternative --with hand-written html-files-- is to wrap each slide in a ``<section>``
                tag. As we want all slides in one md-file, that is not an option.
