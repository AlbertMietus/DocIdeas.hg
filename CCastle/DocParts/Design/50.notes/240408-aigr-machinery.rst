AIGR nodes for Machinery (240408)
=================================
.. uml::

   @startuml

   class AIGR

   package machinery {

   class DispatchTable {
     handlers: List
   }
   DispatchTable <|-- eDispatchTable
   note right: Event DispatchTable

   abstract send_proto {
     + outport
     # receiver
     # handlers: DispatchTable
     - index:
   }
   send_proto  <|-- sendStream
   send_proto  <|-- sendData
   send_proto  <|-- sendEvent

   send_proto -> DispatchTable

   class connection {
     - out: <outport, component>
     - in:    <inport,  component>
     # protocol
   }

   }
   AIGR <|--machinery

   class EventHandler
   note left: A component-callable\n per event (in a Protocol),\n per port
   Entity Port
   'protocol  Protocol
   class  Protocol
   metaclass Component

   connection  *->  Port: out
   connection  *->  Port: in
   connection  ..   Protocol : _indirect_
   Protocol    ..   Port
   Port "*" <-* Component

   eDispatchTable      ->    "*"  EventHandler
   eDispatchTable  "1" <-*   "1"  Port
   Component           *-->  "*" EventHandler

   @enduml


