.. include:: /std/localtoc.irst

.. _Castle-TheSieve:

============================
The sieve demo (start/DRAFT)
============================

.. post::
   :category: CastleBlogs, Demo
   :tags: Castle, DRAFT


   To show many features of CCastle -and to verify them-, I use “the sieve”; which is short for the `Sieve of
   Eratosthenes <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`__. An old, well known algorithm to find prime
   numbers.
   |BR|
   And impliciet concurrent.

   With an almost trivial implementation, many “CC concepts” are shown. In only a handful of lines.

The design
**********

We only need tree or four, simple components for this algorithm, and two protocols.

.. include:: ./sieve-design.irst

The elements of the sieve
=========================

CCastle use “components” [#not-package]_ as main decomposition. Each kind of component can be instantiated multiple
times; which often are also called *component*. One can also use the term *element*, to denote it is one (of possible)
many instantiated component-types. This is very ,like *“classes” vs “objects”* [#active-class]_.


Generator
---------

This component generates just numbers, which will be tested for prime (see below). As primes are always integer bigger
then one; it output is the stream stream of numbers: 2,3,4, …

Sieve (parameterised)
---------------------

We use a (growing) chain of sieve-elements. Each behavior is the same; except for the constant that it gets when
creating. That number is a prime; as will see below.

Each Sieve tries to divide each incoming number to its own, already known prime-number. When the modulo isn’t zero, we
call it a *coprime* (relative to the already tested primes) and send downstream. When it can be divided, the number is
clearly not prime and ignored

Finder
------

Each number that comes out of the chain of sieves is a prime (that is the algorithm; see Wikipedia for details). It is
collected by the finder. And for each found prime, an extra sieve (element) is created and added to the chain. This kind
of shifts the finder to the right (aka downstream)

In some implementations that is the responsibility of the finder (therefore sometimes calls “head”). In a variant, the
‘main’ component is caring that load.

Main
====

All the components (or elements) above have to created (statically or dynamically) by an top-level component, which is
usually called “main”. However the name is not special (like in C/C++), it’s  more a convention (like in Python).

Communication
=============


XXXX

----------

.. rubric:: Footnotes

.. [#not-package]
   A CCastle **component** is unrelated to an *UML-component*. It is **not** a package, as many people use for the UML variant.

.. [#active-class]
   A (CCastle) **component** (or actually, an element) is sometimes described as an “active class (aka object)” -- a
   class with a thread inside. This is not completely correct, but gives a good, first impression.
   |BR|
   Notice however, there a no threads in CCastle -- just concurrency and parallelism.



..  LocalWords:  coprime
