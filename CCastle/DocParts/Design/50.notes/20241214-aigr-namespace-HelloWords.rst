=================================================
NameSpaces: an analyse by the HelloWorld variants
=================================================
:Date: 14 Dec 2034

A NameSpace basically records `names` in a given scope, with pointers to the variable (etc) that is intended by that
nane. The same name in another NameSpace is usually another “thing”.
|BR|
Not only variables have names, almost everything in Castle -that as a name- is recorded in a NameSpace.

* NameSpaces can be *nested*
  a new/sub scope is a namespaces, but is may refer to a name in the outer scope. Also,
* NameSpaces can be imported
  making those names locally available (in python: ``from there import here``
* NameSpaces are hierarchical.
  When `A` is/has a NameSpaces `A.b` referes to **b** insite that NameSpace

Quest
=====

The question are

1) How are those NameSpace(s) represented in the AIRG

   a) And how are the ‘names’ and the ‘things’ stored (and refered)

2) How are language construct, that start a scope, represented in the ARIG?

   a) Some parts are trivia;

      - Each file is a NameSpace; we use :class:`Source_NS` for that

   b) How about f.e. :class:`<ComponentImplementation>`

      - *IS* that class an NameSpace, or
      - *HAS* it a NameSpace (attribute)

   c) Where are the edges?

      - the name of the Component is in the outer NameSpace, but
      - the names of parameters etc?

We will study this by a simple Castle programma: HelloWorld.Castle.
|BR|
The ‘elemental’ variant has only 11 lines of code...

Scopes of ‘Elemental’
=====================

File
----
Castle has (strict) filescope (like python). And so we need a :class:`Source_NS` for the file

* The name of the Source_NS NameSpace is the basename of file
* The complete filename is stored in the ``source`` attribute
* It contains the top-level ‘things’:

  - the docstring (name: __doc__, for now) -- as in python. This is optional
  - the name: `Elemental_HelloWorld` for class :class:`ComponentImplementation`

Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * When ‘things’ are imported, the name of those things are also in that :class:`Source_NS`
         - the name in the NameSpace can be different
           ``import org as thing``

   .. tab:: credible

      * This variant has a protocol too. So the `Source_NS` contains that to
      * Name: `Execute`, thing: :class:`EventProtocol`


   .. tab:: primitive

      * This variants has 5 ‘things’ in filescope. The docstring, a protocol, a component (definition), and two
        implementations of components
      * All 1+4 are in the filescope NameSpace

        - Name: `Execute`, 		thing: :class:`EventProtocol`
        - Name: `HW_Command`,		thing: :class:`ComponentInterface`
        - Name: `HW_Command`,		thing: :class:`ComponentImplementation`
        - Name: `Primitive_HelloWorld`	thing: :class:`ComponentImplementation`

        .. caution::

           *HW_Command* is used twice, ones as Interface and ones to Implement it. This should be possible

           But how do we store that. Is the namespace a dict to a set?
        
.. seealso::

   * :ref:`TestDoubles-HelloWorlds`    -- intro about the HelloWorlds TestDoubles
   * :ref:`HelloWorld_CastleCode_ref`  -- Shows the (CastleCode) of the HelloWorld variants

     In this analyse, the :ref:`xcross-elemental_HW` variant is mostly used
