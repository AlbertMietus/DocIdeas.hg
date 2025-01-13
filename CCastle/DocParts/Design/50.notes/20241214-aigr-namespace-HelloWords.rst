=================================================
Namespaces: an analyse by the HelloWorld variants
=================================================
:date: 14+15 Dec 2024

A namespace basically records `names` in a given scope, with pointers to the variable (etc) that is intended by that
nane. The same name in another namespace is usually another “thing”.
|BR|
Not only variables have names, almost everything in Castle -that as a name- is recorded in a namespace.

* Namespaces can be *nested*
  a new/sub scope is a namespaces, but is may refer to a name in the outer scope. Also,
* Namespaces can be imported
  making those names locally available (in python: ``from there import here``)
* Namespaces are hierarchical.
  When `A` is/has a namespaces `A.b` referes to **b** insite that namespace

.. tip::  nested-namespace and hierarchical-namespaces are not the same.

   * When an ID is not defined in the current scope, it’s not in the current namespaces.
     When searching for that ID, it can be found in a wider scope: the *outer_namespace*
   * When searching for an *“dotted-name”* (`a.b`), and `a` is/has a namespace,
     that namespace is used to find the rest of the name.

Quest
=====

The question are

1) How are those namespace(s) represented in the AIRG

   a) And how are the ‘names’ and the ‘things’ stored (and refered)

2) How are language construct, that start a scope, represented in the ARIG?

   a) Some parts are trivia;

      - Each file is a namespace; we use :class:`Source_NS` for that

   b) How about f.e. :class:`<ComponentImplementation>`

      - *IS* that class an namespace, or
      - *HAS* it a namespace (attribute)

      .. hint:: In Castle’s AIGR this is solved by :class:`_hasScope` 

   c) Where are the edges?

      - the name of the Component is in the outer namespace, but
      - the names of parameters etc?

We will study this by a simple Castle programma: HelloWorld.Castle.
|BR|
The ‘elemental’ variant has only 11 lines of code...

Scopes of ‘Elemental’
=====================

File
----
Castle has (strict) filescope (like python). And so we need a :class:`Source_NS` for the file

* The name of the Source_NS namespace is the basename of file
* The filename is stored in the ``source`` attribute
* It contains the top-level ‘things’:

  - Name: ``__doc__``, (for now) 	thing: the docstring, as in python.     This is optional
  - Name: ``Elemental_HelloWorld`` 	thing: the class :class:`ComponentImplementation`

Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * When ‘things’ are imported, the name of those things are also in that :class:`Source_NS`
         - the name in the namespace can be different
           ``import org as thing``

   .. tab:: credible

      * This variant has a protocol too. So the `Source_NS` contains that to
      * Name: ``Execute``, thing: :class:`EventProtocol`


   .. tab:: primitive

      * This variants has 5 ‘things’ in filescope. The docstring, a protocol, a component (definition), and two
        implementations of components
      * All 1+4 are in the filescope namespace

        - Name: ``Execute``, 		 thing: :class:`EventProtocol`
        - Name: ``HW_Command``,		 thing: :class:`ComponentInterface`
        - Name: ``HW_Command``,		 thing: :class:`ComponentImplementation`
        - Name: ``Primitive_HelloWorld`` thing: :class:`ComponentImplementation`

        .. caution::

           *HW_Command* is used twice, ones as Interface and ones to Implement it. This should be possible ...
           |BR|
           But how do we store that. Is the namespace a dict to a set?


Elemental_HelloWorld
--------------------
The Component (implementation) `Elemental_HelloWorld` is/has a namespace, which contains all ‘things’ inside.

* The callables  (methods, data-/event-handlers, etc):

  - `HelloWorld(str:label))` 		name: ``HelloWorld``, 			thing: :class:`Method`
  - `powerOn(max) on self.power`	name: mangle(``Power``, ``powerOn``, ``power``)	thing: :class:`EventHandler`

* Some ‘edges’

  - Name ``self`` -- the reference to th component-element itself.

Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * When a Component (etc) has a docstring, it is added.
      * ToDo	

   .. tab:: credible

      * ToDo	

   .. tab:: primitive

      * ToDo	

HelloWorld(str:label)
---------------------
Also this method is/has a namespace - which is small. It hardly defined ‘things’ inside.

* However, the (name of) the parameter(s) are valid inside (the body of HelloWorld).

  - Name: ``label``	thing: the parameter ‘label’

.. note::

   The called function ‘HelloWorld’ is *NOT* is the namespace -- it’s not a defined name. It is **used** an can be find
   in the parent-ns: `Elemental_HelloWorld`


Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * ToDo	

   .. tab:: credible

      * ToDo	

   .. tab:: primitive

      * ToDo	

      


powerOn(max) on self.power
--------------------------
This EventHandler, with the mangled name: ``Power::powerOn::power``, again is/has a namespace. Like above the ‘things’
inside are registered in this namespace.

* Again, this namespace only contain “the edges”.

  - Name: ``max``  	-- the parameter of the eventhandler
  - Name: ``power``	-- the port on which event detected.



Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * ToDo	

   .. tab:: credible

      * ToDo	

   .. tab:: primitive

      * ToDo	

      
------------------------------

Variants
~~~~~~~~

.. tabs::

   .. tab:: General

      * ToDo	

   .. tab:: credible

      * ToDo	

   .. tab:: primitive

      * ToDo	

----------------------------------





        
.. seealso::

   * :ref:`TestDoubles-HelloWorlds`    -- intro about the HelloWorlds TestDoubles
   * :ref:`HelloWorld_CastleCode_ref`  -- Shows the (CastleCode) of the HelloWorld variants

     In this analyse, the :ref:`xcross-elemental_HW` variant is mostly used
