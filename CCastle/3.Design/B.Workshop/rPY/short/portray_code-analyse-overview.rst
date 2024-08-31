===========================
Overview CastleCode portray
===========================

When translating CastleCode into RPy code, a valid RPY identifier is needed for every name (like an ‘ID’) used in the source code. On one hand, this translation should be stable, repeatable & predicable. But at the same time any valid CastleCode should result in a valid RPy (aka python) name -- and never in a keyword of the backend.
|BR|
We call this transformation “to portray”; describe and depict the source-code in an particular way (so that can be used by the (selected) Translator

The Sieve: CastleCode & RPy
===========================

In this article we study the well known :ref:`Castle-TheSieve`.
|BR|
See that link for the used code: chapter: *Castle implementation*; Tab: Sieve.

.. list-table:: **Sieve-Component** *implementation*
   :header-rows: 1

   * - AIGR
     - “CC text”
     - RPY in ``SieveClass.py``
     - portray:
     - notes
   * - :class:`ComponentImplementation.ID==‘Sieve’`
     - “implement **Sieve** {”
     - ``CC_Sieve``
     - ``CC_`` prefix
     - see remark on `__init__`
   * - :class:`VariableDefintion.ID==‘MyPrime’`
     - “int **myPrime**;”
     - ``self.myprime`` = ...
     -
     - a line in __init__
   * - :class:`VariableDefintion.type==‘init’`
     - “**int** myPrime;”
     - init(onPrime:``int``)
     - TypeHint (only)
     - *“typing” needs more design*
   * - :class:`Method.ID==‘int’`
     - “**init** (int:onPrime)”
     - ``_castle_init``
     - special: for init
     - See note on __init__
   * - :class:`Method(‘init’)*TypedParameter.ID==‘onPrime’` 
     - “init(int: **onPrime** )”
     - self._castle_init(``onPrime``` =args[0])
       |BR|
       self.myPprime = ... ``onPrime``
     -
     - in `__init__`
       |BR|
       in `_castle_init`
   * - :class:`  .ID==‘’`
     - “ line *id*”
     - ``CC_``
     - ``?`` pre/suffix
     - _note_
   * - :class:`  .ID==‘’`
     - “ line *id*”
     - ``CC_``
     - ``?`` pre/suffix
     - _note_
   * - :class:`  .ID==‘’`
     - “ line *id*”
     - ``CC_``
     - ``?`` pre/suffix
     - _note_
   * - :class:`  .ID==‘’`
     - “ line *id*”
     - ``CC_``
     - ``?`` pre/suffix
     - _note_




-------------

.. list-table:: OLD
   :header-rows: 1

   * - *Castle Code* (context)
     - text (focus)
     - (AIGR) Type/context
     - *RPY*
     - portray:
     - notes
   * - implement Sieve {
     - “Sieve”
     - :class:`ComponentImplementation`
     - ``CC_Sieve``
     - ``CC_`` prefix
     - 
   * - implement Sieve {
     - 
     - 
     - ``__init__``
     - The init method is generated as part of “implement”
     - The ‘init’ in castleCode results in ``_castle_init``
   * - int myPrime;
     - “myPrime”
     - :class:`VariableDefintion`
     - ``myPrime``
     - 
     - 
   * - init(int:onPrime) {
     - “init”
     - :class:`Method`
     - ``_castle_init``
     - *special*
     - see remark on `__init__`; which calls ``_castle_init``
   * - init(int:onPrime) {
     - “onPrime”
     - :class:`TypedParameter`
     - ``onPrime``
     - 
     - 
   * - super.init();
     - “super”
     - :class:`Part`
     - ``super()``
     - In RPy: call
     - Never a call/parameters in CastleCode; in RPY always empty call
   * - super.init();
     - “init”
     - :class:`Method`
     - ``__init__``
     - special
     - see remark on `__init__`
   * - .myPrime := onPrime;
     - “myPrime”
     - :class`Become` (targets)
     - 
     - 
     -
   * - .myPrime := onPrime;
     - “onPrime”
     - :class`Become` (targets)
     - 
     - 
     -
   * - “SimpleSieve.input(try) on .try”
     - 
     - :class:`EventHandler`
     - ``SimpleSieve_input__try```
     - mangle/RPY style
     - the AIGR-ID *may* be used as guidance
   * - 
     - “try”
     - :class:`ID` (name of port
     - ``try_```
     - ``_`` suffix
     - `try` is reserved in python
   * -
     - “”
     - :class:``
     - ``x```
     - ````` pre/suffix
     - _note_
   * -
     - “”
     - :class:``
     - ``x```
     - ````` pre/suffix
     - _note_
   * -
     - “”
     - :class:``
     - ``x```
     - ````` pre/suffix
     - _note_
