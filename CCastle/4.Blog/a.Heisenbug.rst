.. include:: /std/localtoc.irst

.. _Castle-Heisenbug:

======================
Heisenbug (start/DRAF)
======================

.. post::
   :category: CastleBlogs, Castle DesignStudy
   :tags: Castle, DRAFT

   In Castle, one can dynamically connect components and send “events” over those connections. Typically this is done as
   an action on an incoming message (see: :ref:`CCC-Actors`). Depending on ‘:ref:`TheMachinery`’, those events can be
   queued and this combination *can result* in a **beautiful Heisenbug**.

   First, let’s explain the Heisenbug, before we give a example. Then we analyse it, show how it can be solved and
   finally formulate a *requirement* how we can prevent this kind of bugs in Castle.


What is a Heisenbug?
====================

The `heisenbug <https://en.wikipedia.org/wiki/Heisenbug>`__ is named to Werner Heisenberg, who described the *“observer
effect”*: when you look closely, the behavior changes. The same can happen to software (bugs). The behavior apparently
changes when you study -or slightly adjust- that code.  Often this is due (small) changes in timing; possibly even in
generated code. Therefore old (oldfashioned), sequential code on slow CPU’s is less likely to have heisenbugs then
concurrent code on fast multi-core systems. It’s also common in threaded programs.

.. include:: ./Heisenbug-sidebar-Sequence.irst

The sieve goes wrong
====================

Also my standard example ‘:ref:`Castle-TheSieve`’ can suffer from this issue. The initial version did work for years,
but failed horrible when another “machinery” was used. After studying this, the bug is simple, and easy to fix.

There are two related timing issues, that (probably only together) result in the Heisenbug. First, we introduce them one
by one, and then show how the combination may fail.


Event-order
-----------

Conceptually, the `Generator` sends (events with) integers to `Sieve(2)`, which may be forward to `Sieve(3)`, then to
`Sieve(5)`, etc. As shown in the **Conceptual sidebar**, we probably like to assume that each integer is fully sieved
before the next int *starts*. This is the classic “sequential view”, we are used too.

However, that isn’t how it works. In Castle the order of events on a connection is defined (*one by one,
sequential*). And given the code, the integer sent by an Sieve comes always later then the incoming one. But that is all
we may assume.
|BR|
The timing of unrelated events on multiple connections is not defined. That order may depends on :ref:`TheMachinery` and
many other factors. Do not, as developer, assume any order -- like I did!

As shown in the **One-by-One sidebar** diagram, this can result that the Generator output all events first. Next, Sieve(2)
takes-out the even integers, then the Sieve(3) process all its input, then Sieve(5), ect.
|BR|
Although we aren’t using concurrency, and it needs hug buffers -- especially when finding big primes-- it does
conceptually work. And so, it is an allowed execution [#ButImprove]_.


Reconnecting
------------

The chain of `Sieve`\s will grow as we find more primes. When an *int* isn’t filtered-out and so reaches the `Finder` a 
*new prime* is found. Then, a new Sieve-component is created and inserted to the chain.
|BR|
This is done by the Main-component (which is signaled by the Finder) [#orVariant]_.

Therefore, `Main` remembers the ``last_sieve`` and reconnects it’s output to the newly creates `Sieve`. And temporally
connects that new-Sieve’s output to the Finder. For every newly found prime this repeats.
|BR|
This detail is shown in the **With Details** sidebar diagram; where the `Finder` and `Main` component, and all message’s
to/from them are shown.

Assuming the initial “conceptual” order, you will see the same Sieve(s) become alive (“new” message), and are added to
the end of the sieve-chain. The integers still flow (now, shown as “try(`int`)” messages) by this sieve.
|BR|
You will aslo notice the `Finder` does indeed find all primes.


The combination
===============

Now lets study how the sieve-chain will grow with a “fast generator”, and the one-by-one order of events is used. This
diagram is shown below.

As we can see in the picture, it goes horrible wrong. No proper sieve is created, and we will find intergers as *4* and
*6* as prime -- clearly this is wrong.
|BR|
With a (very) *fast Generator*, **all** intergers are send to the `Finder` --before any `Sieve` is created, and so any
int is reported as prime. And, as for each found “prime” a Sieve-component is created, to many elements are added to the
chain. On top of that, no integer is ever sieved....

This is just **an** example. As we can’t predict (or assume) any order, we can find other results too. And, when we add
“debugging print statement” (and *look closer*), we change the timing and will find other results. We found the
*observer effect*!

.. uml:: ./sieve-Sequence-Wrong.puml


.. warning::

   It is not *“the timing”* that is wrong!
   |BR|
   A concurent programm is only correct when it goes right for **any** possible timing.

   As in all SW-engineering, we can prove it is buggy when it goes wrong at least once. That is what we have shown. And
   so, the original code is *wrong*.

How to improve?
===============

xxxxx

SlowStart
---------

xxxxx

Simulation
----------

xxxx


-----

.. rubric:: Footnotes

.. [#orVariant]
   Again, there are many variants of :ref:`Castle-TheSieve`. In some adding a `Sieve` to the chain is done by the `Finder`,
   in others by `Main`. In both alternatives, the same reconnect is needed. There is no real difference  -- but the name
   of the component  initiating the change.
   |BR|
   The Heisenbug will not (trivially) disappear when switching between hose variants

.. [#ButImprove]
   Still, as language-designer, we need to give the programmer more options to hint to a more optimals implementation. 

..  LocalWords:  heisenbugs, heisenbug
