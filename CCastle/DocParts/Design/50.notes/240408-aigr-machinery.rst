AIGR nodes for Machinery (240408)
=================================
.. uml::

   @startuml

   class AIGR

   package machinery {

   class "machinery" as M {
   delegate: implementation
   }
   note right #aquamarine
      There are many Machineries (options).
      All implementation details are
      stored the the delegate.
      (None when abstract)
   endnote


   abstract DispatchTable {
     handlers: List
   }
   DispatchTable <|-- eDispatchTable
   note right: **E**vent DispatchTable

   abstract send_proto {
     + outport
     # receiver
     # handlers: DispatchTable
     - index:
   }
   note left #aqua
      This represents a
      line-of-code to
      **send** event/data
      over a connection
   end note
   class sendStream <<ToDo>> {}
   class sendData  <<ToDo>> {}
   class sendEvent {}
   send_proto  <|-- sendStream
   send_proto  <|-- sendData
   send_proto  <|-- sendEvent

   send_proto -> DispatchTable

   class connection {
     - out: <outport, component>
     - in:    <inport,  component>
     # protocol
   }
   note right #aqua
     This is the result of
     a line-of-code that
     connects two ports
   endnote
   M <|--- send_proto
   M <|--- connection
   M <|--- send_proto
   M <|--- DispatchTable

   }
   AIGR <|--M

   class EventHandler
   note left: A component-callable\n per event (in a Protocol),\n per port
   Entity Port
   'protocol  Protocol
   class  Protocol
   'metaclass Component
   class Component

   connection  o->  Port: out
   connection  o->  Port: in
   connection  ..   Protocol : //indirect//
   Protocol    ..   Port
   Port "*" <-* Component

   eDispatchTable      ->    "*"  EventHandler
   eDispatchTable  "1" <...  "1"  Port
   Component           *-->  "*" EventHandler

   @enduml


