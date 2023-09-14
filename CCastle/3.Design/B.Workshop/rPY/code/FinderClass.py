# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
# Hi-lock: (("^ *def [^:]+:" (0 (quote info-title-4) prepend)))
# Hi-lock: (("^ *class [^:]+:" (0 (quote info-title-3) prepend)))
# Hi-lock: (("=== TRACE:?" (0 (quote ediff-fine-diff-Ancestor) prepend)))
# Hi-lock: (("@@ TRACE:?" (0 (quote ediff-fine-diff-C) prepend)))

from CC import buildin
from CC import base
from CC import _debug
from CC import machinery

import FinderMoat
import SimpleSieve


"""///CastleCode
implement Finder {
///end"""


class CC_Finder(buildin.CC_B_Component) : # Generated class;
    """Each CastleCode ``implement {name} result in a generated class  CC_C_${name-of-component}

    That class is a subclass of the (also generated} class CC_C_${name-of-baseclass}, as specified in the Moat/interface.
    As we can use inheritance, the "isa-pointer" is only mentioned in the top-base class. Also "the machine" is hidden there.

    Here, the CastleCode is ``component Finder : Component ...``, and so Finder is a subclass of `Component`;  where Component
    is the buildin base component.

    .. warning:: generated classes vs filled-in objects

       Don't confuse **CC_C_{name}** (a generated class) with ``CC_B_ComponentInterface`` and/or
       ``CC_B_ComponentClass``, which are *"buildin data-structures,* that are instantiated (and
       filled) to describe a component.

    The  CC_C_{name} classes are runtime instantiated only and hold the (data) storage of a component (element)

    .. tip::  namespace vs prefix for callable(s) (unlike  handCompiled.c*)

       Here --in (r)Python-- the CC_C_{name} scope contain all methods of the component-methods.
       Therefore we don't need the component-name infix, and names are shorter; compared with the C-backend.

       The C function ``CC_E_Finder__SimpleSieve_input__newPrime()`` for event `input` in the `SimpleSieve` protocol,
       connected to the `newPrime` port of the `Finder` can be called ``CC_E_SimpleSieve_input__newPrime()``;  even the
       *CC_E_* prefix is optional. As the (CC_C_)Finder class is used as namespace."""

    def __init__(self, *args):                                                   #NOTE: **kwags not supported in rPython
        #First, the inherited members                                            #GAM: Py2&3 & static version of super()
        buildin.CC_B_Component.__init__(self, isa=cc_C_Finder)
        # Then the outports (not the inport)
        self.found = buildin.CC_B_OutPort()
        # Then the local/member vars
        self._castle_init()

    def _castle_init(self):
        pass

    def _debug_attr_(self, name_only=True):
        # Same order as __init__
        if name_only:
            return buildin.CC_B_Component._debug_attr_(self, name_only=name_only)
        else:
            return (buildin.CC_B_Component._debug_attr_(self)
                        + ", self.found=" + self.found._debug_(name_only=name_only)
                        )


    # GAM/Note: As the methods are 'in' the CC_Finder namespace, the '*_Finder' prefix is not needed ...
    #           ... ``CC_E_Finder__SimpleSieve_input__newPrime`` => SimpleSieve_input__newPrime

    def SimpleSieve_input__newPrime(self, foundPrime):   # handCompiledC: CC_E_Finder__SimpleSieve_input__newPrime
        """///CastleCode
        SimpleSieve.input(foundPrime) on self.newPrime
        {
          self.found.input(foundPrime);
        }
        ///end"""

        print ("@@ TRACE: %s.SimpleSieve_input__newPrime foundPrime=%s" % (self._debug_(name_only=True), foundPrime))

        outport  = self.found;               assert isinstance(outport,  buildin.CC_B_OutPort), "outport is not CC_B_OutPort, but %s" % type(outport)
        receiver = outport.connection;
        if not receiver:
            print ("=== TRACE `self.found` not connected :: skip")
        else:
            assert isinstance(receiver, buildin.CC_B_Component), "receiver is not  CC_B_Component[aka: CC_ComponentType], but %s" % type(receiver)
            handlers = outport.handlers;         assert handlers,  "handlers shouldn't be None, nor an empty list"
            handler = handlers[SimpleSieve.CC_P_SimpleSieve_input]
            print ('=== TRACE trigger .found.input:: receiver=%s, handler=%s' % (receiver._debug_(), _debug.handler_name(handler)))

            # XXX REFACTOR:  do not hard-code the Machinery :-)
            assert  machinery.Machinery == machinery.DirectCall, "Only 'machinery.DirectCall' is supported"
            handler(receiver, foundPrime)
        return
#End CC_Finder


cc_C_Finder = buildin.CC_B_ComponentClass(
    interface = FinderMoat.cc_CI_Finder,
    methods = [],                                 # XXX Is this needed? As the are 'in" CC_Finder"
    isa = None,                                   # Later: use for meta-classes; For now isa is optional
    #instance_size = sys.getsizeof(CC_Finder),  Not needed for rPython
    )

cc_S_Finder_newPrime = [
    None, None, None, None, None, None, # 0-5: not relevant here
    CC_Finder.SimpleSieve_input__newPrime # 6/CC_P_SimpleSieve_input
    ]
assert SimpleSieve.CC_P_SimpleSieve_input == 6, " Event should be on the correct index"
assert cc_S_Finder_newPrime[SimpleSieve.CC_P_SimpleSieve_input] == CC_Finder.SimpleSieve_input__newPrime



def debug(name_only=False):
    from CC import _debug
    # Remember: print for Python 2&3
    print ("DEBUG: " + _debug.file_stem(__file__))
    print ("The generated class:: CC_Finder()")
    print ("< " + CC_Finder()._debug_(name_only=name_only))
    print ("> cc_C_Finder=" + cc_C_Finder._debug_(name_only=name_only))


