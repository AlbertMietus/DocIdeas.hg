# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
#// We are using the (unfinshed `3.NoHeisenbug/CC-event-sieve.Castle` version
"""///CastleCode (Moat part)
protocol SimpleSieve : SlowStart(1) {
  input(int:try);
}
///end"""


from CC import buildin
from CC import base

import SlowStart

CC_P_SimpleSieve_input = 6         # XXX

cc_P_SimpleSieve = buildin.CC_B_Protocol(name = "SimpleSieve",
                                             kind = None,                          # Not given ==> use inherit_from.kind
                                             inherit_from = SlowStart.cc_P_SlowStart,
                                             base_arguments = (1,),
                                             events = [])
cc_P_SimpleSieve.events.append(
    buildin.CC_B_P_EventID(name="input",
                               seqNo=CC_P_SimpleSieve_input,
                               part_of=cc_P_SimpleSieve))
"""///.. ToDo:: (Moat part)

          * seqNo (now -1).
            - Either set it during the CCastle- analyse.
            - Or calc in rPython by adding length of inherit_from chain
          * signature of events
            In "handCompiled-C code, we use a typedef ...(..._FT)... **functionprototype**
"""



def debug():
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("\t" + cc_P_SimpleSieve._debug_(name_only=False))
    SlowStart.debug()

