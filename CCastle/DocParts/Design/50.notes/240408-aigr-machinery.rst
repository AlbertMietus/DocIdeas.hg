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

    class send_proto {
      +outport
      #reviever
      #handlers: DispatchTable
      -index:
    }
    send_proto  <|-- sendEvent
    send_proto  <|-- sendData
    send_proto  <|-- sendStream

    send_proto -> DispatchTable

    class connection {
      - out: <outport, component>
      - in:    <inport,  component>
      # protocol
    }

    }
    AIGR <|--machinery

    class Port
    class Protocol
    class Component

    connection  *-> Port: out
    connection  *-> Port: in
    connection  ..  Protocol
    Protocol .. Port
    Port .* Component

    @enduml
