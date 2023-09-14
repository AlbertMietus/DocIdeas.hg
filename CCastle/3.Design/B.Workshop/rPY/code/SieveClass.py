# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
# Hi-lock: (("^ *def [^:]+:" (0 (quote info-title-4) prepend)))
# Hi-lock: (("^ *class [^:]+:" (0 (quote info-title-3) prepend)))
# Hi-lock: (("=== TRACE:?" (0 (quote ediff-fine-diff-Ancestor) prepend)))
# Hi-lock: (("@@ TRACE:?" (0 (quote ediff-fine-diff-C) prepend)))

from CC import buildin
from CC import base
from CC import _debug
from CC import machinery

import SieveMoat
import SimpleSieve

"""///CastleCode
implement Sieve {
  int myPrime;
///end"""

class CC_Sieve(buildin.CC_B_Component) : # Generated class;

    def __init__(self,  *args):                                                   #NOTE: **kwags not supported in rPython
        #First, the inherited members                                            #GAM: Py2&3 & static version of super()
        buildin.CC_B_Component.__init__(self, isa=cc_C_Sieve)
        # Then the outports (not the inport)
        self.coprime = buildin.CC_B_OutPort()
        # Then the local/member vars
        self._castle_init(onPrime=args[0])
        print ("=== TRACE Created: %s" % self._debug_(name_only=False))

    def _castle_init(self, onPrime):                                      # In handCompiledC: C_Mi_Sieve__init
        """///CastleCode
        -init(onPrime:int)
        {
          super.init();								//note 'super' acts as a port
          self.myPrime := onPrime;
        }
        ///end"""
        self.myPrime=onPrime

    def _debug_attr_(self, name_only=True):
        # Same order as __init__
        if name_only:
            return buildin.CC_B_Component._debug_attr_(self, name_only=name_only)
        else:
            return (buildin.CC_B_Component._debug_attr_(self)
                        + ", self.coprime=" + self.coprime._debug_(name_only=name_only)
                        + ", .myPrime=%s" % self.myPrime
                        )

    #GAM Note: ``try`` is not an allowed var in python; use try_
    def SimpleSieve_input__try(self, try_):   # handCompiledC: CC_E_Sieve__SimpleSieve_input__try
        """///CastleCode
        SimpleSieve.input(try) on .try
        {
          if ( (try % self.myPrime) !=0 ) {
            self.coprime.input(try);
          }
        }
        ///end"""

        print ("@@ TRACE: CC_Sieve.SimpleSieve_input__try(%s, try=%s)" % (self._debug_(name_only=True), try_))

        if try_ % self.myPrime:
            outport = self.coprime; assert isinstance(outport,  buildin.CC_B_OutPort), "outport is not CC_B_OutPort, but %s" % type(outport)
            receiver = outport.connection
            if not receiver:
                print ("=== TRACE (Sieve) `self.coprime` not connected :: skip")
            else:
                assert isinstance(receiver, buildin.CC_B_Component),   "receiver is not  CC_B_Component[aka: CC_ComponentType], but %s" % type(receiver)
                handlers = outport.handlers;         assert handlers,  "handlers shouldn't be None, nor an empty list"
                handler = handlers[SimpleSieve.CC_P_SimpleSieve_input]
                print ('=== TRACE (Sieve) trigger .coprime.input():: receiver=%s, handler=%s' % (
                    receiver._debug_(), _debug.handler_name(handler)))
                # XXX REFACTOR:  do not hard-code the Machinery :-)
                assert  machinery.Machinery == machinery.DirectCall, "Only 'machinery.DirectCall' is supported"
                handler(receiver, try_)
        return
#End CC_Sieve


cc_C_Sieve = buildin.CC_B_ComponentClass(
    interface = SieveMoat.cc_CI_Sieve,
    methods = [],                                 # XXX Is this needed? As the are 'in" CC_Sieve"
    isa = None,                                   # Later: use for meta-classes; For now isa is optional
    #instance_size = sys.getsizeof(CC_Sieve),  Not needed for rPython
    )


cc_S_Sieve_try = [
    None, None, None, None, None, None, # 0-5: not relevant here
    CC_Sieve.SimpleSieve_input__try,   # 6/CC_P_SimpleSieve_input
    ]
assert SimpleSieve.CC_P_SimpleSieve_input == 6, " Event should be on the correct index"
assert cc_S_Sieve_try[SimpleSieve.CC_P_SimpleSieve_input] == CC_Sieve.SimpleSieve_input__try


def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("The generated class:: CC_Sieve(-42)")
    print ("< " + CC_Sieve(-42)._debug_(name_only=name_only))
    print ("> cc_C_Sieve=" + cc_C_Sieve._debug_(name_only=name_only))


