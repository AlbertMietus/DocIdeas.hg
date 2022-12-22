=========================================
Modeling & Rendering Components & Friends
=========================================

.. hint:: Sources

  * ModelMore.ipynb, which is baed on
  * Model-GCD.ipynb

  Currently (Dec 12, 2022), this file (`CCastle2/IPython/Components.py` is most updated one

.. todo::
   Spilt the Modeling & Rendering parts; by using delegating to a ${Any}Rendering subclasses of ${Any}

.. caution:: The text below needs to converted from MD to RST
             
Overview
=========

Each component has 3 structures to fully describe the component; most are generated and/or filled by the compiler.

**CC_B_ComponentInterface**
   Describes the interface (as by the Moat file)
**CC_B_ComponentClass**
   Describe a component (as class) (as by the Castle-file)
*CC_C_${CompName}*
   Characterises each instance for component *${CompName}*.

   This is handled by :class:`CC_Component`

The first two are predefined (build-in) structures that are filled (and named) by the compiler.
The last one is defined (```#typedef```) by the compiler.

For each component that is *coded* in a Castle file, the structures `CC_B_ComponentInterface` and a
`CC_B_ComponentClass` are filled (read: a variable of that type is instancianted); they get the name
cc_CI_\\${*CompName*}** resp **cc_C_${*CompName*}**. 
<br/>
And, a new structure `CC_C_${CompName}` is defined (but not instanciated); the size of that struct depend on the component. As components do inherite, the structure-fiels of all super-components tripple down in the (top of) the new structure!  This implies all `CC_C_${CompName}` structures start by ("inherite from") the baseComponent -- which struct is called CC_**B**_Component

#### <span style="color:blue">Notes</span>

* The names of the structures & variables are based on the *"handCompiled"* version; they can/will change. But need to be alligned
* The variables ("instances") start with **cc_**; in small-case
* The structures ("classes") start in **CC_**; in captial
* Therefore, cc_C_\\${CompName} and CC_C_\\${CompName} are not the same. The first is a instance of a CC_B_ComponentClass, the second is a generated type (for the same component
* This can be a bit confusing. Probally I will change the name(s)

#### Prefix/Infix/Suffix
* Components
  - <span style="background: lightblue;">\_CI\_</span> (infix)
    stands for **C**omponent-**I**nterface,
  - <span style="background: lightblue;">\_C\_</span> (infix)
    stands for **C**omponent (implementation). 
  - <span style="color: purple;">Probally beter abrivations will help</span>
* The infix <span style="background: lightblue;">\_B\_</span> 
  stands for **B**uildin
* The prefix <span style="background: lightblue;">CC\_</span>
  is alike CCaste

Below we show the rendering of **CC_C_${CompName}** first. And them the other two; However, the need details al **`port`** & **`protocols`**; so the are defined too.
