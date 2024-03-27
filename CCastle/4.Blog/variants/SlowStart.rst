:orphan:
.. (C) 2024 Albert Mietus. Part of CCastle project

.. _SLowStart-Sieve:

======================
SlowStart Sieve (ToDo)
======================

* variants [#sieve-variants]_,

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


.. [#sieve-variants]
   There are multiple variants of ‘the Sieve’; all showing other (CC/Castle) aspects. In this one event-bases protocols
   are used. There is also a variant with data-based protocol, variants with, and without :ref:`Castle-Heisenbug`, etc.


.. tabs::

   .. code-tab:: ReasonML try() on found -- with puhback

      // We have build the sievelist (and reconnect) on a newly found prime ..
      SimpleSieve.try(newPrime) on self.generator.found
      {
        alias s;

        // Extent the sieve-list ...
        s:= Sieve.new(newPrime);
        s.coprime = self.finder.newPrime;
        if (not self.lastSieve == Ground) {              // .lastSieve == Ground, so not connected, so we have the first Sieve to connect to .generator
          self.generator.outlet = s.try;
          self.generator.outlet.queue.removeLimit();
        } else {
          self.lastSieve.coprime = s.try;
          self.lastSieve.coprime.queue.removeLimit();
        }
        .lastSieve := s;

        self.generator.collect.input(newPrime);   // forward the prime to the Generator
      }

