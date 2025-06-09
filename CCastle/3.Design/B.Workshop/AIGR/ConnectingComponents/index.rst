=================================
Connecting Components (AIGR view)
=================================


A fundamental concept in CCastle is the connection between components; by `Port`\s and `Protocol`\s. The implementation
of a component can not *'reach'* (or “see”) anything outside it own `Component`. It can only react on data on an
(incoming) `Port`, and sent data (like events) over an (outgoing) `Port`.

In this chapter we examine how that conceptually works and which data-structures in a AIGR are needed to capture
it. For simplicity we limit ourselves to `Event`\s (and so `EventProtocol`\s & `Eventhandler`\s) for now. Other kinds,
like “Data”, “Stream” are added later.

Primary Classes
===============
Let’s start with an overview of the dataclasses in the AIGR, that are fundamentally to connect component and
communicate with event.

.. uml:: PClasses.puml

* The :class:`ComponentInterface` & :class:`ComponentImplementation` describe the `Component`. One with an external
  aspect, and one with the internal parts -- the later are “hidden”
* The (incoming and/or outgoing) :class:`Port`\s are “visible” -- they are listed in the `ComponentInterface`.
* Assuming the PortType is ‘Event’, it is linked to a :class:`EventProtocol`. Which contains a list of :class:`Event`\s
* Notice: As both the :class:`ComponentInterface` and the :class:`Protocol` support sub-classing, one should ponder the
  inherited Ports & Events too -- see the fields :attr:`based_on`
* An :class:`Eventhandler` --visible only inside it Component-- will be triggered depending on the :class:`Port` and an
  :class:`Event` within a specific :class:`Protocol` --either explicitly given by the Castle-programmer, or deducted by
  the :class:`Port` [#deductedProto]_

--------------

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

   */index
   *

.. rubric:: Footnotes

.. [#deductedProto]
   In CastleCode one is allowed to name only the Event and Port name, then de compiler will deducted the Protocol (as
   the port has a type aka Protocol). Or, one can fully specify it, so with the protocol-name as prefix for the Event.
   |BR|
   Conceptually, a single port can listen to multiple Protocols; but as long event-names are unique (relative those
   Protocols) this will work. Moreover, this multi-protocol option is not yet supported.

   In the AIGR, however, the full set is specified; always!

