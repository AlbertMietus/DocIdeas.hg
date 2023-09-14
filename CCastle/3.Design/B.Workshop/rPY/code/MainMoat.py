# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
"""///CastleCode  (Moat part)
component Main : Board {}
///end"""

## Board is empty for now
## ///CastleCode  (Moat part)
## component Main : Board {} // Board is empty for now
## ///end

from CC import buildin
from CC import base

cc_CI_Board = buildin.CC_B_ComponentInterface(name = "Board",
                                                 inherit_from   = base.cc_CI_Component,
                                                 ports          = [])
# XXX ToDo: add a port to start?
## run, start, powerOn, ...
## tick, next, step, ...

cc_CI_Main = buildin.CC_B_ComponentInterface(name = "Main",
                                                 inherit_from   = cc_CI_Board,
                                                 ports          = []) # No port (for now)



#///  Moat part is done

def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("> cc_CI_Board=" + cc_CI_Board._debug_(name_only=name_only))
    print ("> cc_CI_Main="  +  cc_CI_Main._debug_(name_only=name_only))

