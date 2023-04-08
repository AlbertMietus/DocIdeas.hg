.. include:: /std/localtoc.irst

.. _Castle-Heisenbug:

=======================
Heisenbugs (start/DRAF)
=======================

.. post::
   :category: CastleBlogs, Castle DesignStudy
   :tags: Castle, DRAFT

   In Castle, one can dynamically connect components, and send “events” over those connections. Typically this is done as
   an action on an incoming message (see: :ref:`CCC-Actors`). Depending on ‘:ref:`TheMachinery`’, those events can be
   queued and this combination *can result* in a **beautiful Heisenbug**.

   First, let’s explain the Heisenbug, before we give an example. Then we analyze it, show how to improve the code, and
   finally formulate a *requirement* to prevent & detect this kind of bug in Castle.

What is a Heisenbug?
====================

The `heisenbug <https://en.wikipedia.org/wiki/Heisenbug>`__ is named to the theoretical physics *Werner Heisenberg*, who
described the *“observer effect”*: when you look closely, the behavior changes. The same can happen to software
(bugs). The behavior apparently changes when you study -or slightly adjust- that code.  Often this is due to (small)
changes in timing; possibly even in generated code. Therefore old (old-fashioned), sequential code on slow CPUs is less
likely to have heisenbugs than concurrent code on fast multi-core systems. It’s also common in threaded programs.

.. include:: ./Heisenbug-sidebar-Sequence.irst

The sieve goes wrong
====================

My standard example, :ref:`Castle-TheSieve`, suffered from this issue. The initial version did work for years,
but failed horribly when another “machinery” was used. After studying this, the bug is simple and easy to fix.

There are two related timing issues, that (probably only together) result in the Heisenbug. First, we introduce them one
by one and then show how the combination may fail.


Event-order
-----------

Conceptually, the `Generator` sends (events with) integers to `Sieve(2)`, which may be forwarded to `Sieve(3)`, then to
`Sieve(5)`, etc. As shown in the **Conceptual sidebar**, we probably like to assume that each integer is fully sieved
before the next *’int’* *starts*. This is the classic “sequential view”, we are used to.

However, that isn’t how it works. In Castle, the order of events on a connection is defined (*one by one,
sequential*). And given the code, the integer sent by a `Sieve` comes always later than the incoming one. That is all we
may assume.
|BR|
The timing of unrelated events on multiple connections is not defined. That order may depend on :ref:`TheMachinery` and
many other factors. Do not as a developer, assume any order --as I did!

As shown in the **One-by-One sidebar** diagram, this can result that the Generator is outputting all events first. Next,
Sieve(2) filters out the even integers, then Sieve(3) processes all its input, then Sieve(5), etc.
|BR|
Although we aren’t using concurrency, and it needs huge buffers -- especially when finding big primes-- it does
conceptually work. And so, it is an allowed execution [#ButImprove]_.


Reconnecting
------------

The chain of `Sieve`\s will grow as we find more primes. When an *int* isn’t filtered-out and so reaches the `Finder` a
*new prime* is found. Then, a new Sieve element is created and inserted into the chain.
|BR|
This is done by the Main component (which is signaled by the Finder) [#orVariant]_.

Therefore, `Main` remembers the ``last_sieve`` and reconnects its output to the newly creates `Sieve`. And temporally
connects that new-Sieve’s output to the Finder. For every newly found prime, this repeats.
|BR|
This detail is shown in the **With Details** sidebar diagram; where the `Finder` and `Main` and all its messages
are shown too.

Assuming the initial “conceptual” order, you will see the same Sieve(s) become alive (“new” message), and are added to
the end of the sieve chain. The integers still flow (now, shown as “try(`int`)” messages) by this sieve.
|BR|
You will also notice the `Finder` does indeed find all primes.


The combination
===============

Now let us study how the sieve chain will grow with a “fast generator”, and the one-by-one order of events is used. This
diagram is shown below.

As we can see in the picture, it goes dreadfully wrong. No proper chain is created, and we will find integers like **4**
and **6**.  This is wrong, they are not prime.
|BR|
With a (very) *fast Generator*, **all** integers are sent to the `Finder` --before any `Sieve` is created, and so any
int is reported as prime. besides, too many elements are added to the chain as a Sieve component is created for each found
“prime”.  On top of that, no integer is ever sieved...

This is just **an** example. As we can’t predict (or assume) any order, we can find other results too. And, when we add
“debugging print statement” (and *look closer*), we change the timing and will find other results. We found the
*observer effect*!

.. uml:: ./sieve-Sequence-Wrong.puml


.. warning::

   It is not *“the timing”* that is wrong!
   |BR|
   A concurrent program is only correct when it goes right for **any** possible timing.

   As in all software engineering, we can prove it is buggy when it goes wrong at least once. That is what we have
   shown. And so, the original code is *wrong*.


How to improve?
===============

Finding this heisenbug triggered an investigation  to improve both Castle and ‘:ref:`Castle-TheSieve`’. Where our goals
is not (just) to improve the sieve code, but all programs. And give the programmer options to prevent heisenbugs.

.. include:: ./sieve-protocols-sidebar.irst

SlowStart
---------


Castle (now) comes [#KipEi]_ with the parametric *base* protocol :ref:`SlowStart <doc-SlowStart>`, which is based on
`TCP Slow start <https://en.wikipedia.org/wiki/TCP_congestion_control#Slow_start>`__ and contains a queue-model
[#ModelOnly]_ to controll the speed off an event-connection. As the name suggests, initially the connections with be
slow. Roughly, the parameter set the maximal number of unhandled events on a connection.
|BR|
The (improved) version of :ref:`Castle-TheSieve` uses a SlowStart of **1**. And `Main` will remove (or increase) that
limit after reconnecting.

Initially, the `Generator` is only *allowed* to sent one event, which is received by the `Finder`. Then `Main` will create
the first Sieve (`Sieve(2)`), reconnects the Generator to that component, and increases the “speed” of the
connection. As the connection **`Generator`->`Sieve(2)`** is stable, the is no need to limit the “queue”.

The `Generator` acts as before: it sends (events with) integers over its output. But now, the SimpleSieve protocol can
slow down the `Generator` --no code changes are needed for this. This may happen when the second event is sent, before
it is received (or “handeld”) by the Finder, and the limit is set to **1**.
|BR|
As this limit is removed when a Sieve-component is inserted to the chain, only the start is slow...

The same happens to every Sieve: initially (when it is connected to the Finder) there is a limit of 1 event in the
queue. But when that connection is reconnected --and the potential Heisenbug is gone-- the limit is removed.

.. tip:: Unlimited or better?

   In this blog we remove the limit of the ``SlowStart protocol`` completely, for simplicity. Than, the Heisenbug is
   solved.

   That is not the only option.
   |BR|
   Given the `Generator` is a simple loop it can produce many integers fast. And so cause huge piles of queued
   events. That can be done better, by the same concept: a maximal queue size. (again: just model).

   It’s up to de developer to optimize this. Some prever the maximum (queue length) equally to the number of
   Sieve-components,  other related it to the available core. Some use static values, other will adjust it over the
   run-time of the appplication.
   |BR|
   That is all possible, with a few extra lines in the `Main` component. But also the Sieve component can set this
   limit, both for incoming-ports as for outgoing port.


Simulation
----------

XXX


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

.. [#KipEi]
   This *SlowStart* base-protocol is part of Castle; see :ref:`Protocol-SlowStart`. But the need for it --follows like
   this blog-- follows from the discovery of this :ref:`Castle-Heisenbug` in :ref:`Castle-TheSieve`.


.. [#ModelOnly]
   Remember, this queue exist as a *model* **only** (like everything in Castle-code)!
   |BR|
   Depending on ‘:ref:`TheMachinery`, there may no need to implement the queue (e.g.with DirectCall) at all; or the may
   only be a queue-lenght and -maximum, or ..



..  LocalWords:  heisenbug heisenbugs
