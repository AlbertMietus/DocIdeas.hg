.. Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017.
   Part of MESS-DocIdeas

.. _dPID_exercise:

==============
dPID: exercise
==============
:status: pre-alpha

TDD-approach
============

Test first
----------

First, write some test-files with test-functions that verify the correct working of the :class:`dpid.dPID` class as specified.
Depending on your knowledge of PID-controllers these test may (functionally) vary. The primary goal here is not to program
(including testing) a great PID-controller; but to practice your python-skills.

.. hint:: time-dependent

   The :class:`dpid.dPID` class is discrete; it only calculates the :meth:`dpid.dPID.result` when requested. This implies the
   (return) value of :meth:`dpid.dPID.result` will depend on when it is called (relative to the other methods).

   * So, timing may be relavant in your (test)-code. One can use ``time.sleep`` to controll that. By using a floating-point
     parameter, this is accurate in the milli-seconds range.

   * By using a (small, relavant) MARGIN when comparing values, small derivations (in e.g. timing) can be compensated.

   .. seealso:: Convenient python functions

      * https://docs.python.org/3.5/library/time.html?highlight=sleep#time.sleep
      * https://docs.python.org/3.5/library/functions.html?highlight=abs#abs

Code second
-----------


And improve (refactor)
----------------------


