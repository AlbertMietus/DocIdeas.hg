.. _ ADR0001:
.. sidebar:: On this page
   :class: localtoc

   .. contents::
      :depth: 6
      :local:
      :backlinks: none

=========================================
ADR_0001: AIGR-tools? (import & packages)
=========================================

.. adr:: AIGR.tools namespace-packages
   :ID: ADR_0001
   :Status: Accepted

   * We adopt the dot-notation.

     - `aigr_extra.scaffolders` will (ultimately) become  ``aigr.tools.scaffolders``.
     - This gives us the freedom to keep scaffolders in the current package, or put it in (later) in another

   * As AIGR (itself) and the **scaffolders** are tightly coupled, we keep the scaffolders in the castle-aigr
     package. (At least  for now; see above, it becomes trivial to change)

   * New aigr-tools will become a new native namespace-package below/in ``castle.aigr.tools``.

     - This includes `Trawlers`.

Context and Problem Statement
=============================

The AIGR itself is clear: it is a data-class collection with no (real) method. To use the AIGR, soms *“AIGR tools”* are
needed. Like the `_Scaffolder` classes  and the (new) “Trawlers”

The question is: where are they located? Both as in which package? And, where in import hierarchy?

The AIGR
---------

* The AIGR --as an IM/AST-- is dataset; even it is currently  available in python only, it is language-agnostic. And
  can’t contain *methods* -- there are a few, but only to set the default containers, etc.
* The AIGR has many types of “nodes” (classes), and will grow to a over a honderd (data)classes
* The AIGR is also a tree with elements of (sub-classes) of the AIGRNode class (a subclass of AIGR)
  |BR|
  That tree can become big: from a few 1000 (one file) to millions (a big program)
* The AIGR (as classes) is extendable; f.e. an component in the pipeline may add types.

Tools
~~~~~

To build, but mostly to read and traverses an AIGR-tree, we need “tools” that abstract the details of the AIGR; and
provide the methods that AIGR needs.

The Scaffolders where introduced early and (temporally) wrap an AIGR-instance, to give it methods. As an example: it
brings functionality to `register` (add) children. Depending on the node and the “kind of child”, the correct
implementation is automatically selected (behind the common interface).
|BR|
Up to now, those Scaffolders are located in the base package *castle-aigr* and available via
`castle.aigr_extra.scaffolding`

New tools
~~~~~~~~~

Recently the need for a new “tool” become prominent: ‘Trawlers’.That (example) package contains classes like `Trawl` to
walk over the AIGR “elements” tree, and to select/search for nodes in a more complicated way. This is roughly modeled
as one can walks over a HTML/XML tree, (like the DOM), using concepts as XPath we can “go a few steps to a node of e
given kind, under the condition that node has minimal 2 children, named such and so”.
|BR|
As an example for the AIGR: “given a call to an method, named “M”, find the formal parameter list of the corresponding
callable definition”. Another one is “find all descendants of `node`, which `.parent` field is not set” (to fix it).

This is clearly more abstract then the Scaffolders, but it will use the Scaffolders.

.. note:: “Trawlers” is work in progress.

   * This ‘Trawlers’ tool is new, and not fully designed.
   * Also the name of the tool/class/packages is not fully set, we as an example here
   * We expect more new tools
   * The name of “Trewlers’ (and other tools) is out of scope of this ADR


Challenges
==========

The basic question is where will this, and further “AIGR-tools” be placed.

It’s tempting to place them in the current package, along `aigr_extra` -- to be used as (f.e.) ``import
castle.aigr_extra.trawlers``.  But this make this “base package” bigger, whereas the idea is that others can bring (&
use) alternative package -- and as such a base package should be minimal.
|BR|
The alternative is to make a new package. Then the question is how to import it. Somehow it is “part” of the aigr, even
it  does not *belong* to it (aka the package).

That question lead to a few more investigations. In short:

1. Should the Scaffolders be part of (the current) castle-aigr package?

2. Is “aigr_extra” the best name? Of should we use `castle.aigr.extra`, `castle.aigr.tools` -- not the dot, making it a
   sub-module (which becomes easier for switching)
   |BR|
   Remember: Using a ‘.’ instead of ‘_’ in a package-name is nowadays considers more pythonic. And enables
   namespaces-packages.

3. What is the border between “Scaffolders” and “Trawlers”? It’s quite clear that “children” s part of Scaffolders -- it
   really depend on the kind of (AIGR)node.
   |BR|
   But how about searching for names -- or types-- in name-spaces? Especially when it traverses thou a chain  of (outer)
   namespaces/scopes?

4. How about even more “tools”


Decision Drivers
----------------

* An important driver is clarity & maintenance, including can we update, or replace, a tool without the need to updating
  other  packages?
* The same of updating the base aigr package, with more/new kinds of nodes. It should never demand that other packages
  are updated directly! (especially not when those new feature are not used/relevant)
* Given the AIGR elements tree can be huge, performance is relevant (but not very). But being able to use an “optimized”
  version of a “tool” can be convent. As a reference: in Python one can use `xml.etree.ElementTree` and/or `lxml.etree`;
  the are equivalent but for speed and easy of installation



Considered Options
==================

Packages & use
---------------

castle.aigr_extra.<tools>:
  Just add the Trawlers into the existing package, as castle.aigr_extra.<trawlers>
castle.aigr.extra.<tools>:
   Rename the current use, from ‘_extra’ to `.extra` and add Trawlers to this sub-package
   |BR|
   In this case it “feels” more independent, and it enables a latter spit of the package
castle.aigr.tools.<tools>:
   Same as above, but renaming extra to tools. That brings more clarity
Sub namespace-packages for <tools>
   A variant of above, where castle.aigr.tools is/contains a namespace-packages itself
   * The each tool can be implemented in an independent packages,
   * A bit of reality check is needed, but it looks very much on the same concepts we have in “readers”
   * It this case, we can decide per “tool” in  which packages it should be implemented.


What is a Scaffolder? What does Trawlers?
-----------------------------------------

#. *Don't worry*. Just keep it asis and add stuff. This speeds-up development, and we don’t have many used. We can always
   change later.
#. *Strict*: Scaffolder focus on single nodes, Trawlers on the tree. -- strict implies move some search functionality.
#. *Loosely*: Scaffolder focus on single nodes, Trawlers on the tree. -- keep searching as is.

Outcome
=======

See :need:`ADR_0001` (above) for main resolution.

Consequences
------------

* Migration: castle.aigr_extra is deprecated; functionality moves to castle.aigr.tools.scaffolders.
* Keep Scaffolders: in castle-aigr package, only change imports etc.
* Study: the scaffolders-methods, that are not strictly none only -- move to other tools is an option
* Implement the Trawlers in a new aigr-<tools> package
* Clear split: Scaffolders handle Node-local logic; Trawlers handle Tree-wide logic.

..  LocalWords:  scaffolders
