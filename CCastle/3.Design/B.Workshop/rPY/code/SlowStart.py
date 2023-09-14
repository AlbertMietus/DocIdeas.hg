# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
#// We are using the (unfinshed `3.NoHeisenbug/CC-event-sieve.Castle` version
"""///CastleCode
////////////NEW SlowStart (protocol)
#Org:
# protocol SlowStart(queue_max:int): EventProtocol {
#  -  setMax(queue_len:int);
# }
#Simplified: (set event, ipv inherit)
protocol SlowStart(queue_max:int):
  kind: event
  -  setMax(queue_len:int);
}
///end"""

from CC import buildin
from CC import base

cc_P_SlowStart = buildin.CC_B_Protocol(name = "SlowStart",
                                           parameters = [('queue_max', int)],
                                           kind = buildin.CC_B_ProtocolKindIs_Event,
                                           inherit_from = None,
                                           events = [])
cc_P_SlowStart.events.append(
    buildin.CC_B_P_EventID(name="setMax",
                               seqNo=-1,                       #XXX
                               parameters = [('queue_max', int)],
                               part_of=cc_P_SlowStart))
#///  Moat part is (mostly) done



"""///CastleCode
////////////NEW SlowStart (implement)
implement SlowStart {
  int queue_len = 0
  int max_len;

-init(queue_max)
{
  self.max_len := queue_max
}

-setMax(queue_len)
{
  self.max_len := queue_len
}

-removeLimit()
{
  self.max_len := -1;
}
'''
.. todo:: HOW TO MODEL:

   * sending an event makes the queue one longer
   * getting ('on' make the queue one shorter
   * When the queue is full: slow down ...
'''
} //end implement SlowStart
///end"""



def debug():
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("\t" + cc_P_SlowStart._debug_(name_only=False))
