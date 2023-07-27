=====================
All Sphinx Directives
=====================
.. Copyright (C) ALbert Mietus, 2018

.. post:: 2018/05/11
   :category: Sphinx
   :tags: Tips & Tricks

   `Sphinx <http:\\Sphinx-doc.org>`_ comes with a huge number of *directives*. Some are inherited from `RST
   <http://docutils.sourceforge.net/rst.html>`_, others come from the many extensions that are available. But the is no
   list of all, or the most used directives in Sphinx.

   Until now ...

.. update:: 2018/05/13

   Added more opensource projects as a reference to show “all” Directives.

The most used directives to document Sphinx itself
==================================================

With a simple iPython-script, I counted all directives in all (`.rst` & `.py`) files of `Sphinx-doc
<https://github.com/sphinx-doc/sphinx.git>`_ (*the latest version, on May 10, 2018*); 1758 in total. The table below
shows them all, sorted in most-used-order.  As you can see many directives are only used once (`0.06%`) or twice ...

.. include:: SphinxDoc.rst.inc

More directives
===============

As promised, I want to show *all* directives. That is hardly possibly, as *RST* (and so, Sphinx) is extendable; anybody
can add directives... Still, we can come close, by scanning more documentation-projects.

The same script can scan several (documentation) projects; by summing the resulting ``DirectiveCounter``\s together, the
big-table below is produced.

Currently, I scan some of my personal projects, and a few open-source ones:

* `cPython      	 <https://github.com/python/cpython.git>`_
* `Needs (sphinxcontrib) <https://github.com/useblocks/sphinxcontrib-needs.git>`_
* `Numpy  		 <https://github.com/numpy/numpy.git>`_
* `Pandas		 <https://github.com/pandas-dev/pandas.git>`_
* `pygments       	 <http://bitbucket.org/birkenfeld/pygments-main>`_
* `ReadTheDocs  	 <https://github.com/rtfd/readthedocs.org.git>`_
* `Scipy                 <https://github.com/scipy/scipy.git>`_
* `Sphinx-doc		 <https://github.com/sphinx-doc/sphinx.git>`_

.. include:: totalCounts.rst.inc

.. note:: Are you missing a directive?

   Find a project using it and let me know! And I will rerun the scripts. And simular when a major documentation-project
   should be included to get better stats.
