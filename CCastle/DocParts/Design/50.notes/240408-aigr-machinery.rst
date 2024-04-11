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

   abstract send_proto {
     + outport
   }
   note top #aqua
      This represents a
      line-of-code to
      **send** event/data
      over a connection
   end note

   class sendStream <<ToDo>> {}
   class sendData  <<ToDo>> {}
   class sendEvent {
     + event: Event
     + arguments: ArgumentList
   }
   send_proto  <|-- sendStream
   send_proto  <|-- sendData
   send_proto  <|-- sendEvent

   abstract DispatchTable {
     handlers: List
   }
   DispatchTable <|-- eDispatchTable

   send_proto -> DispatchTable

   class connection {
     + outport: <outport, component>
     + inport:    <inport,  component>
   }
   note top #aqua
     This is the result of
     a line-of-code that
     connects two ports
   endnote
   M <|--- send_proto
   M <|--- connection
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

   'Port  <-* Protocol  : uses
   Port "*" <-* Component

   eDispatchTable      ->    "*"  EventHandler
   eDispatchTable  "1" <...  "1"  Port
   Component           *-->  "*" EventHandler

   Entity Event {
     # name
     # index:key
   }
   note left #aquamarine: Basically, a name in a Protocol (definition),\n and (also) the key (index/number) in a DispatchTable
   sendEvent o--> Event

   Event "1".. "*" EventHandler
   Event .> Protocol: > part of

   @enduml

