# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))

"""///CastleCode  (Moat part)
component Finder : Component {
  port SimpleSieve<in>:newPrime;
  port SimpleSieve<out>:found;
}
///end"""

from CC import buildin
from CC import base

import SimpleSieve


cc_CI_Finder = buildin.CC_B_ComponentInterface(name = "Finder",
                                                   inherit_from   = base.cc_CI_Component,
                                                   ports          = [])
"""
.. note:: About configuring port[] with append *afterwards*

   I don't like/prefer this approach, but as the ports contain a reference to the ComponentInterface
   (``cc_CI_Finder`` here), we have to. Otherwise, it does not compile."""
cc_CI_Finder.ports.append(
    buildin.CC_B_C_PortID(name="newPrime",
                              portNo=2,
                              protocol=SimpleSieve.cc_P_SimpleSieve,
                              direction=buildin.CC_B_PortDirectionIs_in,
                              part_of=cc_CI_Finder))
cc_CI_Finder.ports.append(
    buildin.CC_B_C_PortID(name = "found",
                              portNo = 3,
                              protocol = SimpleSieve.cc_P_SimpleSieve,
                              direction = buildin.CC_B_PortDirectionIs_out,
                              part_of = cc_CI_Finder))
#///  Moat part is done



def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("> cc_CI_Finder=" + cc_CI_Finder._debug_(name_only=name_only))

