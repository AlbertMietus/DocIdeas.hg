.. .. include:: /std/localtoc.irst

.. _Castle-TheSieve:

============================
The Sieve demo (start/DRAFT)
============================

.. post::
   :category: CastleBlogs, Demo
   :tags: Castle, DRAFT


   To show some features of CCastle, I use *‘the sieve’*, short for the `Sieve of Eratosthenes
   <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`__. An old, well known, algorithm to find prime numbers; with
   impliciet concurrency.

   With an almost trivial implementation, many “CC concepts” can be shown. In only a handful of lines....

The design
**********

We only need tree simple components as shown below, and a main component (not shown). We also use two protocols, that
are given below.

.. include:: ./sieve-design.irst

The elements of the sieve
=========================

CCastle use “components” [#not-package]_ as main decomposition. Each kind of component can be instantiated multiple
times; sometimes called a *element*, or also just *component*. This is very like *“classes” and “objects”* in OO
[#active-class]_.

Let’s introduce the those components

Generator
---------

This component generates just numbers, which will be tested for prime (see below). As primes are always integer bigger
then one; it output is the stream stream of numbers: 2,3,4, …

Sieve (on prime)
----------------

We use a (growing) chain of sieve-elements. Each one is the same; except for the sieving-constant --a already found
prime. That number is set when instantiating the element.


Each Sieve tries to divide each incoming number to its own, sieve-constant. When the modulo isn’t zero, we call it
a *coprime* (relative to the already tested primes) and send downstream. When it can be divided, the number is clearly
not prime and ignored

Finder
------

Each number that comes out of the chain of sieves is a prime (that is the algorithm; see Wikipedia for details). It is
collected by the finder. For each found prime, an extra sieve (element) is created and added to the chain. This kind
of shifts the finder to the right (aka downstream)

In some implementations that is the responsibility of the finder (therefore sometimes calls “head”). In a variant, the
‘main’ component is caring that load.

Communication
=============
.. include:: ./sieve-protocols-sidebar.irst

CCastle uses “protocols” to communicate between components. There are several kind of protocols; we use the ‘event’ kind
here. Two ports can be connected when both use the same protocol.

Notice, that a *protocol* is not the same as an API in most language’s. A fundamenta concept of :ref:`CC`/CCastle is the
strict seperation between outside and inside

StartSieve
----------

The StartSieve protocol signals to start sieving (so generating numbers), and when to stop. This “max” number is the
maximal number to be tried, and does not need to be a prime.

Currently, the is no way to specify the number of primes to be found.


SimpleSieve
-----------

In this variant [#sieve-variants]_, we use an event-based protocol, that just hold one event (read: a message), that
carries the integer to be tried.

In the *Original* version, it was a basic `Protocol`. Which worked fine until we studied the another :ref:`machinery
<TheMachinery>`: :ref:`Machinery-LibDispatch`, and it become clear we had a :ref:`Castle-Heisenbug`! (See there for
details.)
|BR|
Now, we use an improved version, where we use a simple push-back algorithm by inheriting from ``SlowStart``. This adds a
queue to the model, that limits (slows down) the sender to a maximum number of (unhandled) events; in this case that is
initially: only one event ``SlowStart(1)``.

.. note::

   Without going into details, it important to realize the *queue* is only added in the model! Depending on the
   :ref:`TheMachinery` it will probably  **not** exist in the computer-code.
   |BR|
   For example, the :ref:`Machinery-DirectCall` machinery will never need, not use this queue

   It also shows normal Castle-programmer can focus on the functional aspect of the protocol. The SimpleSieve doesn't
   need any extra message to controll this SlowStart (or sliding windows, as is also know) algorithm. That is fully
   handled in a generic base-protocol.
   |BR|
   Additionally, the even more technical aspect of how to send events between (CC) components are completely hidden. As
   long as both components use the same protocol it will work. ref:`TheMachinery` will make sure that both components
   use the same technical details on both ends.



Main
****

All the components (or elements) above have to created (statically or dynamically) by an top-level component, which is
usually called “main”. However the name is not special (like in C/C++), it’s  more a convention (like in Python).




XXXX

The Code
********

.. include:: ./sieve-code.irst

----------

.. rubric:: Footnotes

.. [#not-package]
   A CCastle **component** is unrelated to an *UML-component*. It is **not** a package, as many people use for the UML variant.

.. [#active-class]
   A (CCastle) **component** (or actually, an element) is sometimes described as an “active class (aka object)” -- a
   class with a thread inside. This is not completely correct, but gives a good, first impression.
   |BR|
   Notice however, there a no threads in CCastle -- just concurrency and parallelism.

.. [#sieve-variants]
   There are multiple variants of ‘the Sieve’; all showing other (CC/Castle) aspects. In this one event-bases protocols
   are used. There is also a variant with data-based protocol, variants with, and without :ref:`Castle-Heisenbug`, etc.


..  LocalWords:  coprime
