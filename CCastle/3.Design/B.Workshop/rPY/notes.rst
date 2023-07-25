================================================
Note: events trigger eventhandler (by Machinery)
================================================

.. seealso::

   * .../SIEVE/1.WorkCopy/CC-event-sieve.Castle-handCompiled.c
   * .../SIEVE/2.GCD-work/CC-event-sieve.Castle-handCompiled.c

.. tip:: The assert & printf/debug statements (in C code) are removed, for clarity

CC_E_Generator__StartSieve_runTo__controll
==========================================
.. code-block:: ReasonML

   self.outlet.input(i);

Generated
---------
.. code-block:: C

    {
    struct CC_B_OutPort          outport   = self->outlet;
    CC_ComponentType             receiver  = outport.connection
    CC_B_eDispatchTable          handlers  = outport.handlers    // This is set during the connect!
    CC_E_SimpleSieve_input_FT    signal    = (CC_E_SimpleSieve_input_FT)handlers[CC_P_SimpleSieve_input]

    signal(receiver, (CC_selfType)self, i);
    }

LibDispatch
~~~~~~~~~~~
Most of the code is the same, but the call the eventhandler:  That line
( ``signal(receiver, (CC_selfType)self, i);``) is the same, but embedded in a dispatch_queue plumbing 

.. code-block:: C

   ... // see above upto/including: ``CC_E_SimpleSieve_input_FT    signal = ...``

   dispatch_queue_t             queue     = receiver->queue;
   dispatch_async(queue, ^{
       signal(receiver, (CC_selfType)self, i);
     });
    }

As we like to focus on the generated structure, we ignore the LibDispatch variant; and only show te DirectCall base

CC_E_Sieve__SimpleSieve_input__try
===================================
.. code-block:: ReasonML

   self.coprime.input(try)

Generated
---------
.. code-block:: C

   {
   struct CC_B_OutPort          outport   = self->coprime;
   CC_ComponentType             receiver  = outport.connection;
   CC_B_eDispatchTable          handlers  = outport.handlers;
   CC_E_SimpleSieve_input_FT    signal    = (CC_E_SimpleSieve_input_FT)handlers[CC_P_SimpleSieve_input];

   signal(receiver, (CC_selfType)self, try);
   }


CC_E_Finder__SimpleSieve_input__newPrime
========================================
.. code-block:: ReasonML

   self.found.input(foundPrime);

Generated
---------
.. code-block:: C

  {
  struct CC_B_OutPort          outport   = self->found;
  CC_ComponentType             receiver  = outport.connection;
  CC_B_eDispatchTable          handlers  = outport.handlers;
  CC_E_SimpleSieve_input_FT    signal    = (CC_E_SimpleSieve_input_FT)handlers[CC_P_SimpleSieve_input];

  signal(receiver, (CC_selfType)self, foundPrime);
  }


CC_E_Main__powerOn__power
=========================
.. code-block:: ReasonML

   self.generator.runTo(max);

This one differs a bit, as ``.generator`` is a **sub**\(component), not a ``port<out>``

.. error::

   Probably, this CCastle code is wrong: a Generator can handle ``runTo``, but only on it’s controll port.
   |BR|
   I assume, the code should be

   .. code-block:: ReasonML

      self.generator.controll.runTo(max);



Generated
---------
.. code-block:: C

  {
  CC_ComponentType          receiver = self->generator;
  CC_B_eDispatchTable       handlers = cc_S_Generator_controll; //XXX =self->generator->"controll"
  CC_E_StartSieve_runTo_FT  signal   = (CC_E_StartSieve_runTo_FT)handlers[CC_P_StartSieve_runTo];

  signal(receiver, (CC_selfType)self, max);
  }

.. warning:: A better variant is, see bug above

  .. code-block:: C

     {
     CC_ComponentType          sub = self->generator; // One extra line to find the sub-component
     struct CC_B_OutPort       outport   = sub->controll
     CC_ComponentType          receiver  = outport.connection;
     CC_B_eDispatchTable       handlers  = outport.handlers; 
     CC_E_StartSieve_runTo_FT  signal   = (CC_E_StartSieve_runTo_FT)handlers[CC_P_StartSieve_runTo];

     signal(receiver, (CC_selfType)self, max);
     }

   
