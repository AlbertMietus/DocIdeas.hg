.. _CCastle2-top:

=============
CCastle Notes
=============

My ambition:

   Castle: '*The best Real-Time/Embedded/Technical/System language*, **EVER**'

   --ALbert Mietus

It’s also the first programming-language that support CC [#CC]_. Where `CC` is kind of of the successor of OO: active
‘things’ that communicate (solely) by input *and* output ports ... 
|BR|
*(Yes, I know, ambition and reality are not always aligned...)*

Castle2
=======
**CCastle2** is the second attempt, and the successor of CC-Castle, a project that is stalled and stopped.

It incorporates moderen SW-Enginering concepts as DSL/MDE *(Model-based development)*; where the domain is Technical
and/or Embedded-Systems. It focuses on high quality ‘always on’ and/or flawless systems; including real-time systems,
kernel-drivers, compilers, etc. It also expects and support both low-end (“cheap”) SoC (System-on-Chip) systems, and
CPU’s with many, many cores (hundreds to thousands!).

DocIdeas
========
This section contains a set of pages & blog-post on this topic. Some a design-studies, some explain how to use the language, some are ... just notes.


‘One day’ the pages will be incorporated into the (docs of, the source of) `CCastle2 <https://osdn.net/users/albertmietus/pf/CCastle2>`_

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   */index

.. seealso:: The :ref:`blog-drafts` page for the *drafts* (all, including Castle ones)



Needs (index)
=============

.. needtable::
   :style: table
   :sort: type
   :columns: id;title;incoming;outgoing;type

.. note:: Old plantUML-version on RTD

   Some UML-diagrams are shown in this section, which are defied by `plantUML
   <https://en.wikipedia.org/wiki/PlantUML>`__. However, `ReadTheDocs
   <http://docideas.mietus.nl/en/ccastle-busy/CCastle/index.html>`__ currently support only an old version (*1.2017.15*;
   **2017**). which has no theme and other support to make it more nice-looking. Therefore all those “lines” are comment
   out (or rewritten)

----------

.. rubric:: Footnotes

.. caution::

   .. [#CC]
       CC can stand for many things; I haven’t decided which one is the official one ....
       |BR|
       Candidates are:

       * Connected Components
       * Concurrent Components
       * Connected & Concurrent
       * Concurrent Connections
       * ...
