# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
# Hi-lock: (("^ *def [^:]+:" (0 (quote info-title-4) prepend)))
# Hi-lock: (("^ *class [^:]+:" (0 (quote info-title-3) prepend)))
# Hi-lock: (("=== TRACE:?" (0 (quote ediff-fine-diff-Ancestor) prepend)))
# Hi-lock: (("@@ TRACE:?" (0 (quote ediff-fine-diff-C) prepend)))

from CC import buildin
from CC import base
from CC import _debug
from CC import machinery

import MainMoat
import StartSieve,  SimpleSieve

import GeneratorClass, SieveClass, FinderClass

"""///CastleCode
implement Main {
  sub generator;
  sub finder;
  alias lastSieve;
///end"""

class CC_Board(buildin.CC_B_Component) : # Generated class;
    def __init__(self,  isa=MainMoat.cc_CI_Board,  *args):
        buildin.CC_B_Component.__init__(self, isa=isa)
        #End init


class CC_Main(CC_Board) : # Generated class;

    def __init__(self,  *args):
        #First, the inherited members; XXX skipping Board
        CC_Board.__init__(self, isa=MainMoat.cc_CI_Main)
        # Then the outports (not the inports)
        # Then the local/member vars
        self._castle_init()

    def _castle_init(self):
        """///CastleCode
        -init()
        {
          self := super.init();

          .generator := Generator.new();
          .finder    := Finder.new();

          .generator.outlet = .finder.newPrime; // Initially, there aren't any Sieves

          self.lastSieve := Ground;

          ??? .finder.found _==> SimpleSieve_input__generator_found ??? HACK "pin"
        }
        ///end"""
        # XXX   ??? self := super.init()
        self.generator = GeneratorClass.CC_Generator()
        self.finder    = FinderClass.CC_Finder()

        #line ``.generator.outlet = .finder.newPrime``
        self.generator.outlet.connection = self.finder
        self.generator.outlet.handlers = FinderClass.cc_S_Finder_newPrime

        #line ``self.lastSieve := Ground``
        self.lastSieve = None

        #line connect hack pin 1 ``.finder.found = self."pin 1"``
        self.finder.found.connection = self
        self.finder.found.handlers = cc_S_Main__pin1 #  handCompiled: `cc_S_Main_pin__generator_found`

    def _debug_attr_(self, name_only=True):
        # Same order as __init__
        if name_only:
            return buildin.CC_B_Component._debug_attr_(self, name_only=name_only)
        else:
            return (buildin.CC_B_Component._debug_attr_(self)
                        + ", sub:generator="    + (self.generator._debug_()  if self.generator else "")
                        + ", sub:finder="       + (self.finder._debug_()     if self.finder else "")
                        + ", alias:lastSieve="  + (self.lastSieve._debug_()  if self.lastSieve else "Ground")
                        )

    def insert_sieve(self, s):
        """ Split out off ``SimpleSieve.input(newPrime) on self.generator.found``
        ///CastleCode
          if (self.lastSieve == Ground) {              // .lastSieve == Ground, so not connected, so we have the first Sieve to connect to .generator
            self.generator.outlet = s.try;
            #self.generator.outlet.queue.removeLimit();
          } else {
            self.lastSieve.coprime = s.try;
            #self.lastSieve.coprime.queue.removeLimit();
          }
          .lastSieve := s;
        ///end"""

        if  not self.lastSieve:
            print ("=== TRACE/CONNECT:\tCastleCode:: ``.generator.outlet = s.try``")
            self.generator.outlet.connection = s
            self.generator.outlet.handlers = SieveClass.cc_S_Sieve_try                #<<< HardCoded DispatchTable
            # XXX ToDo 		self.generator.outlet.queue.removeLimit()
        else:
            print ("=== TRACE/Connect:\tCastleCode:: ``lastSieve.coprime = s.try``")
            self.lastSieve.coprime.connection = s
            self.lastSieve.coprime.handlers = SieveClass.cc_S_Sieve_try              #<<< HardCoded DispatchTable
            # XXX ToDo		self.lastSieve.outlet.queue.removeLimit()
        self.lastSieve = s

    def SimpleSieve_input__finder_found(self, newPrime):
        """///CastleCode
        SimpleSieve.input(newPrime) on self.finder.found
        {
          alias s;

          s:= Sieve.new(newPrime);
          s.coprime = self.finder.newPrime;

          ///split-out
          //if (self.lastSieve == Ground) {              // .lastSieve == Ground, so not connected, so we have the first Sieve to connect to .generator
          //  self.generator.outlet = s.try;
          //  #self.generator.outlet.queue.removeLimit();
          //} else {
          //  self.lastSieve.coprime = s.try;
          //  #self.lastSieve.coprime.queue.removeLimit();
          //}
          //.lastSieve := s;

          .generator.collect.input(newPrime);   // forward the prime to the Generator
        }
        ///end"""
        print ("@@ TRACE: %s. SimpleSieve_input__finder_found(%s)" % (self._debug_(name_only=True), newPrime))

        s = SieveClass.CC_Sieve(newPrime); s._set_label('s%s' % newPrime)

        s.coprime.connection = self.finder
        s.coprime.handlers = FinderClass.cc_S_Finder_newPrime

        self.insert_sieve(s)

        #line:``.generator.collect.input(newPrime)``   // forward the prime to the Generator
        print ("=== TRACE/trigger-direct:\tCastleCode:: ``self.generator.collect.input(newPrime)`` ??")

        receiver = self.generator
        if not receiver:
            print ("=== TRACE receiver `self.generator` not connected :: skip")
        else:
            # XXX REFACTOR:  do not hard-code the Machinery :-)
            GeneratorClass.cc_S_Generator_collect[SimpleSieve.CC_P_SimpleSieve_input](self.generator, newPrime)


    def powerOn__power(self, max):
        """///CastleCode
        powerOn() on self.power
        {
          int max := 10; ///GAM update: now  a parameter 

          self.generator.runTo(max);
        }
        ///end"""
        print ("@@ TRACE: %s.powerOn__power(s)" % (self._debug_(name_only=True),))

        GeneratorClass.cc_S_Generator_controll[StartSieve.CC_P_StartSieve_runTo](self.generator, max)
#End CC_Main


cc_C_Main = buildin.CC_B_ComponentClass(
    interface = MainMoat.cc_CI_Main,
    methods = [],                                 # XXX Is this needed?
    isa = None,                                   # Later: use for meta-classes; For now isa is optional
    #instance_size = sys.getsizeof(CC_Main),        Not needed for rPython
    )

CC_P_Power_On = 1
cc_S_Main_power = [
    None,
    CC_Main.powerOn__power,
    ]
assert CC_P_Power_On == 1, "Trivials - set above"
assert cc_S_Main_power[CC_P_Power_On] ==     CC_Main.powerOn__power

cc_S_Main__pin1 = [
    None, None, None, None, None, None, # 0-5: not relevant here
    CC_Main.SimpleSieve_input__finder_found, # 6/CC_P_SimpleSieve_input
    ]
assert SimpleSieve.CC_P_SimpleSieve_input == 6, " Event should be on the correct index"
assert cc_S_Main__pin1[SimpleSieve.CC_P_SimpleSieve_input] == CC_Main.SimpleSieve_input__finder_found



def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("The generated class:: CC_Board()")
    print ("< " + CC_Board()._debug_(name_only=name_only))
    print ("The generated class:: CC_Main()")
    print ("< " + CC_Main()._debug_(name_only=name_only))


