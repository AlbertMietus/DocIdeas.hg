=================================
Connecting Components (AIGR view)
=================================

A fundamental concept in CCastle is the connection between components; by `Port`\s and `Protocol`\s. The implementation
of a component can’t *see* ( or '*reach'*) anything outside it own `Component`. It can only react on data on an
(incoming) `Port`, and sent data (like events) over an (outgoing) `Port`.

In this chapter we examine how that conceptually works and which data-structures in a AIGR are needed to capture
it. For simplicity we limit ourselves to `Event`\s (and so `EventProtocol`\s & `Eventhandler`\s) for now. Other kinds,
like “Data”, “Stream” are added later.

Primary Classes
===============
Let’s start with an overview of the dataclasses in the AIGR, that are fundamentally to connect components by
communicating with events.

.. uml:: PClasses.puml

* The :class:`ComponentInterface` & :class:`ComponentImplementation` describe the `Component`. One with an external
  aspect, and one with the internal parts -- the later are “hidden”.
  |BR|
  Notice that both are *named* -- and will have the same name.
* The external aspects of the :class:`Port` class are “visible”; they are mentioned in the `ComponentInterface`.  Aside
  of it’s name, its direction (like incoming) and type are also visible.
  |BR|
  Here we assume its type is an (Event)Protocol.  Then, the :class:`Port` links to an :class:`EventProtocol`; which is a
  specialization of :class:`Protocol`.
* The :class:`EventProtocol` contains a list of :class:`Event`\s. As events are sent from component to component, they
  are clearly “visible”.
* The :class:`Eventhandler`\s however, are “hidden” and invisible outside the Component (Implementation).
  |BR|
  They are triggered by the external event, and associated with a :class:`Port`,  and an :class:`Event` within a specific
  :class:`Protocol` [#deductedProto]_.

  .. note:: As both :class:`ComponentInterface` and :class:`Protocol` support sub-classing, one should ponder the
            inherited Ports & Events too -- see the fields :attr:`based_on`.


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

