.. _EventIndex:

=========================
Modelling the Event Index
=========================

A (Castle) Event is like a remote function-call, to another Component.
|BR|
For a Castle-programmer an event is just a name, and always defined within the scope of a (Event)Protocol. But
internally, the event is used as an index in a DispatchTable.

Question
=========
The (design) question is how/where to model that index: Is it an attribute of the Event, or of the Protocol? Or ...
|BR|
For the :ref:`Castle-WorkshopTools` developers, this is an important detail. The number should be stable: in one
Component the DispatchTable is filled, using those indexes, in another it is used to calculate that index to make the
call -- and depending on :ref:`TheMachinery`, it is possible those sides are independent (even on other computers!).

Concept
-------
Conceptually, the order of the Events in a Protocol determine the number; where inherited events become before new ones.

.. Note:: It is not possible to use the name of the Event as a hash value.

   That would make a simple and unique number. But the collection of Events (aka a Protocol) wouldn't be a *consecutive
   series*, and so not suitable in most (low level) implementation languages (C, Assembly, etc)

   Also, adding an event (when e.g subclassing an Event) can result reordering of the sequence, which is not
   allowed. New event should be added “at the end”.

Options
=======
.. error::

   The :ref:`AIGR` (currently) does not has a *backlink* from `Event` to `Protocol`.

   This implies the analyse below is partly wrong:
   |BR|
   As we can’t look-up the Protocol of an `Event` code, a method as ``Event.eventIndex(self) -> int`` can’t be
   implemented.

   .. warning::

      Although it’s correct that the (current) :ref:`AIGR` has no backlink, this is strange, as most backends do have
      that backlink.


Event-attribute
---------------

We can just number the event, and store that number in the event-dataclass. This is simple, but as some complications

* Although an event is always “inside” a protocol, it is possible that two (or more) protocols use the same name (and
  even types/signatures) for an event with those protocols.

  - Strictly speaking, this results in two (or more) the Event dataclasses, each with the same name (attribute). And so,
    it not a limitation. But is can be confusing

* To determine the number (of an event), we need the protocols scope anyhow

  - There is no other way to set the number: find the number if inherited events, and continue counting ...

So, it is possible to store the number in the Event. But we need the protocol too: both to select the event (e.g when
there are several with the same name, in multiple protocols. And to determine the sequence-number.

Protocol-Attribute
------------------

As all events are already “in” a protocol, we can also that (Protocol) dataclasses to determine and store the number --
or just calculate it when needed

Abstraction
-----------

It is also possible to combine it, by abstracting from the details.
|BR|
Both the Event- and Protocol (data)class can be used to query the index. Then it is not relevant where it is exaclty
stores (if at all). Then, that becomes an implementation detail

This is the option we propose.

Solution
========

Currently, we  can only find the index of an Event by asking the Protocol. It is moduled to the standard
*sequence*.index() method:

.. code-block:: python

   Protocol.eventIndex(self, event: Event) -> int

This will search the inherited protocols as well as the specified one.
