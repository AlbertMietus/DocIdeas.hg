# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
"""///CastleCode (Moat part)
component Sieve(onPrime:int) : Component {
  port SimpleSieve<in>:try;
  port SimpleSieve<out>:coprime;
}
///end"""

from CC import buildin
from CC import base

import SimpleSieve


cc_CI_Sieve = buildin.CC_B_ComponentInterface(name = "Sieve",
                                                   inherit_from   = base.cc_CI_Component,
                                                   ports          = []) # GAM:SEE Note in FinderMoat

cc_CI_Sieve.ports.append(
    buildin.CC_B_C_PortID(name="try",
                              portNo=2,   # GAM: why start at 2??
                              protocol=SimpleSieve.cc_P_SimpleSieve,
                              direction=buildin.CC_B_PortDirectionIs_in,
                              part_of=cc_CI_Sieve))
cc_CI_Sieve.ports.append(
    buildin.CC_B_C_PortID(name="coprime",
                              portNo=3,
                              protocol=SimpleSieve.cc_P_SimpleSieve,
                              direction=buildin.CC_B_PortDirectionIs_out,
                              part_of=cc_CI_Sieve))

#///  Moat part is done



def debug(name_only=False):
    # Remember: print for Python 2&3
    from CC import _debug
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("> cc_CI_Sieve=" + cc_CI_Sieve._debug_(name_only=name_only))
