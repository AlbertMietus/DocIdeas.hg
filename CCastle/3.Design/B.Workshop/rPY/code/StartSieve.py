# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
"""///CastleCode (Moat part)
protocol StartSieve : Protocol {
  kind: event;
  runTo(int:max);
  newMax(int:max);
}
///end"""


from CC import buildin
from CC import base

CC_P_StartSieve_runTo    = 7       # XXX Now arbitrary number, simulating 7 [0:6] inherited events
CC_P_StartSieve_NoEvents = 8       # XXX This number is ``CC_P_StartSieve_runTo+1``


cc_P_StartSieve = buildin.CC_B_Protocol(name = "SimpleSieve",
                                            kind = buildin.CC_B_ProtocolKindIs_Event,
                                            inherit_from = None,
                                            events = [])
cc_P_StartSieve.events.append(
    buildin.CC_B_P_EventID(name="runTo",
                               seqNo=CC_P_StartSieve_runTo,
                               part_of=cc_P_StartSieve))
cc_P_StartSieve.events.append(
    buildin.CC_B_P_EventID(name="newMax",
                               seqNo=CC_P_StartSieve_NoEvents,
                               part_of=cc_P_StartSieve))

def debug():
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("\t" + cc_P_StartSieve._debug_(name_only=False))


