.. -*- coding: utf-8 -*-
.. Copyright (C) Albert Mietus, use, copy, modify at wil

.. _admon-use:

Admonitions (overview & use)
============================

.. post:: 2023/7/27
   :category: Sphinx
   :tags: Tips & Tricks

   Sphinx (and RST) support several “admons” or `admonitions
   <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives>`__ to make the reader aware
   of hazard or other parts of text that should stand out. But it hardly tells anything on which to use, in which case.

   Therefore, I list them and give some advise when to use them

And, you can also see how the look like. Note however, the rendering depends on your configuration, especially the
*style* (aka: which **ccs**) is used.

Frequently used
---------------

.. error:: Use  ``.. error::`` when tools/process can go wrong, and can't continue.

   This directive notices the user (or manual-reader) when things really (can) go wrong. This implies and the
   tool/process can't continue.

   .. hint:: Although this admonition is in the *frequently used* list, a sound design & documentation should
	     minimize the number of *errors*, and so this admonition  shouldn't be seen often.

.. warning::

   The ``.. warning::`` directive is to signal on "tricky" items. Probably it *can* be correct, but often it will
   **wrong** So, it's not an ``error``, and the tool/process can continue -- possible with a wrong output.

.. caution:: Use ``.. caution::`` to warn the reader about the document itself.

   E.g. when the document does **not** have the same status/release as the product/tool and can be misleading.
   |BR|
   Now the solution is typical to update the docs.

.. hint:: A ``.. hint::`` is like a positive caution.

   It always targets the (typical) reader of the document.

.. important:: Use ``.. important::`` as a notice to a **fellow/delegate writer**

   .. note:: Typical not in a final/delivered document.

   This is used to describe what kind of information should be writen in that article/section.

.. note:: A ``.. note::`` is just a generic note


Hardly used
------------

.. danger:: This is even more wrong than en ``error``; possible *life-threading*.

   Therefore the ``.. danger::`` directive should hardly be used; not is software tools.


.. admonition:: generic admonition

   The generic ``..admonition::`` (with parameter!) can be used when no standard admonition is available. Use
   reluctantly 


