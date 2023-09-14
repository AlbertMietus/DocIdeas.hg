# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
"""///CastleCode  (Moat part)
component Generator : Component {
  port StartSieve   <in>  : controll;
  port SimpleSieve  <out> : outlet;
  port SimpleSieve  <in>  : collect;
}
///end"""

from CC import buildin
from CC import base

import StartSieve
import SimpleSieve



cc_CI_Generator = buildin.CC_B_ComponentInterface(name = "Generator",
                                                   inherit_from   = base.cc_CI_Component,
                                                   ports          = []) # GAM:SEE Note in FinderMoat

cc_CI_Generator.ports.append(
    buildin.CC_B_C_PortID(name="controll",
                              portNo=2,   # GAM: why start at 2??
                              protocol=StartSieve.cc_P_StartSieve,
                              direction=buildin.CC_B_PortDirectionIs_in,
                              part_of=cc_CI_Generator))
cc_CI_Generator.ports.append(
    buildin.CC_B_C_PortID(name="outlet",
                              portNo=3,
                              protocol=SimpleSieve.cc_P_SimpleSieve,
                              direction=buildin.CC_B_PortDirectionIs_out,
                              part_of=cc_CI_Generator))
cc_CI_Generator.ports.append(
    buildin.CC_B_C_PortID(name="collect",
                              portNo=3,
                              protocol=SimpleSieve.cc_P_SimpleSieve,
                              direction=buildin.CC_B_PortDirectionIs_in,
                              part_of=cc_CI_Generator))

#///  Moat part is done

def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("> cc_CI_Generator=" + cc_CI_Generator._debug_(name_only=name_only))
