# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
# Hi-lock: (("^ *def [^:]+:" (0 (quote info-title-4) prepend)))
# Hi-lock: (("^ *class [^:]+:" (0 (quote info-title-3) prepend)))
# Hi-lock: (("=== TRACE:?" (0 (quote ediff-fine-diff-Ancestor) prepend)))
# Hi-lock: (("@@ TRACE:?" (0 (quote ediff-fine-diff-C) prepend)))

from CC import buildin
from CC import base
from CC import _debug
from CC import machinery

import GeneratorMoat
import StartSieve,  SimpleSieve
 
"""///CastleCode
implement Generator {
  int maxValue;
///end"""
class CC_Generator(buildin.CC_B_Component) : # Generated class;

    def __init__(self,  *args):                                                   #NOTE: **kwags not supported in rPython
        #First, the inherited members                                            #GAM: Py2&3 & static version of super()
        buildin.CC_B_Component.__init__(self, isa=cc_C_Generator)
        # Then the outports (not the inports)
        self.outlet = buildin.CC_B_OutPort()
        # Then the local/member vars
        self._castle_init()

    def _castle_init(self):                                      # In handCompiledC: C_Mi_Sieve__init
        self.maxValue=-1 #int
        self._SimpleSieve_input__collect__count = 0 # static

    def _debug_attr_(self, name_only=True):
        # Same order as __init__
        if name_only:
            return buildin.CC_B_Component._debug_attr_(self, name_only=name_only)
        else:
            return (buildin.CC_B_Component._debug_attr_(self)
                        + ", self.outlet=" + self.outlet._debug_(name_only=name_only)
                        )

    def StartSieve_newMax__controll(self, max_):
        """///CastleCode
        StartSieve.newMax(max) on self.controll
        {
          self.maxValue := max;
        }
        ///end"""
        print ("@@ TRACE: %s. StartSieve_newMax__controll(max=%s)" % (self._debug_(name_only=True), max_))
        self.maxValue = max_

    def StartSieve_runTo__controll(self, max_):
        """///CastleCode
        StartSieve.runTo(max) on self.controll
        {
          int i;

          self.maxValue := max;
          i:=2;
          while (i < self.maxValue) {
            self.outlet.input(i);
            i++
          }
        }
        ///end"""
        print ("@@ TRACE: %s. StartSieve_runTo__controll(max=%s)" % (self._debug_(name_only=True), max_))

        self.maxValue = max_
        i = 2
        while i < self.maxValue:
            outport = self.outlet; assert isinstance(outport,  buildin.CC_B_OutPort), "outport is not CC_B_OutPort, but %s" % type(outport)
            receiver = outport.connection
            if not receiver:
                print ("=== TRACE<i=%s> `self.coprime` not connected :: skip" % i)
            else:
                assert isinstance(receiver, buildin.CC_B_Component),   "receiver is not  CC_B_Component[aka: CC_ComponentType], but %s" % type(receiver)
                handlers = outport.handlers;         assert handlers,  "handlers shouldn't be None, nor an empty list"
                handler = handlers[SimpleSieve.CC_P_SimpleSieve_input]
                print ('=== TRACE(<i=%s>trigger .outport.input:: receiver=%s, handler=%s' % (
                    i, receiver._debug_(), _debug.handler_name(handler)))

                # XXX REFACTOR:  do not hard-code the Machinery :-)
                assert  machinery.Machinery == machinery.DirectCall, "Only 'machinery.DirectCall' is supported"
                handler(receiver, i)
            i +=1
        return

    def assertCorrectPrime(self, foundPrime):
        if self._SimpleSieve_input__collect__count < len(TEST_PRIMES):
            assert TEST_PRIMES[self._SimpleSieve_input__collect__count] == foundPrime, (
                "Sorry found an ERROR: prime is the wrong one; expected %s, got %s" %
                (TEST_PRIMES[self._SimpleSieve_input__collect__count], foundPrime))


    def SimpleSieve_input__collect(self, foundPrime):
        """///CastleCode
        SimpleSieve.input(foundPrime) on .collect
        {
          static int count:=0; //This is a instance var of Generator, with a scope of SimpleSieve.input
          count :+= 1;
          //printf("Generator: Collected %8ith prime: %8i", count, foundPrime);
          // GAM: formatting as ``%8i`` is not supported in rPython -- for now use %s with updated formate:
          printf("Generator: Collected prime (no %s): %s", count, foundPrime);
        }

`        ///end"""

        print ("@@ TRACE: %s. SimpleSieve_input__collect(foundPrime=%s)" % (self._debug_(name_only=True), foundPrime))
        self.assertCorrectPrime(foundPrime)

        # in _castle_init: self._SimpleSieve_input__collect__count=0
        self._SimpleSieve_input__collect__count +=1
        print ("Generator: Collected prime (no: %s): %s" % (
            self._SimpleSieve_input__collect__count, foundPrime))


        return
#End CC_Generator


cc_C_Generator = buildin.CC_B_ComponentClass(
    interface = GeneratorMoat.cc_CI_Generator,
    methods = [],                                 # XXX Is this needed?
    isa = None,                                   # Later: use for meta-classes; For now isa is optional
    #instance_size = sys.getsizeof(CC_Generator),  Not needed for rPython
    )


cc_S_Generator_controll = [
    None, None, None, None, None, None, None,  # 0-6: not relevant here
    CC_Generator.StartSieve_runTo__controll,   # 7
    CC_Generator.StartSieve_newMax__controll,  # 8
    ]
assert StartSieve.CC_P_StartSieve_runTo == 7, "Event should be on the correct index"
assert cc_S_Generator_controll[StartSieve.CC_P_StartSieve_runTo] == CC_Generator.StartSieve_runTo__controll

cc_S_Generator_collect = [
    None, None, None, None, None, None,        # 0-5: not relevant here
    CC_Generator.SimpleSieve_input__collect,   # 6
    ]
assert SimpleSieve.CC_P_SimpleSieve_input == 6, "Event should be on the correct index" 
assert cc_S_Generator_collect[SimpleSieve.CC_P_SimpleSieve_input] == CC_Generator.SimpleSieve_input__collect


def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("The generated class:: CC_Generator()")
    print ("< " + CC_Generator()._debug_(name_only=name_only))
    print ("> cc_C_Generator=" + cc_C_Generator._debug_(name_only=name_only))
    print ("+tDispatchTable(s)")
    print ("\tcc_S_Generator_controll=" + str(cc_S_Generator_controll))
    print ("\tcc_S_Generator_collect="  + str(cc_S_Generator_collect))

TEST_PRIMES= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] # the first 25 
