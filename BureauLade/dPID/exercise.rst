.. Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017.
   Part of MESS-DocIdeas

.. _dPID_exercise:

==============
dPID: Exercise
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

   * So, timing may be relavant in your (test)-code. One can use ``time.sleep`` to controll that. Usa a floating-point
     parameter for sub-second resolution. Typically, the function is accurate in the milli-seconds range.

   * Compare using a small *MARGIN*, to allow derivations due e.g. timing. See the :ref:`examples <dPID_test_examples>`.

   .. seealso:: Convenient python functions

      * https://docs.python.org/3.5/library/time.html?highlight=sleep#time.sleep
      * https://docs.python.org/3.5/library/functions.html?highlight=abs#abs

Instructions
~~~~~~~~~~~~

* Use the `pytest <https://pytest.readthedocs.io>`__ framework, to shorten tests-code.

  - :ref:`pytest_into` is a summary with everything you need for this exercise.
  - You can use :ref:`dPID_test_examples` as *template* for your own files.

* Start by running ``pytest`` as shown.

  - Reproduce the shown output first, before adding your own files.
  - Remember; the output text will differ slightly; for paths, dates etc.

* Add a (one) new file: ``test_<something>.py``.

  - Copy the start of the file (above the first function); update the copyright.
  - Write a single test-function:

    * Create a :class:`dpid.dPID` instance with known, **simple** ``P``, ``I`` and ``D`` settings.
    * Give it a :meth:`~dpid.dPID.setpoint` and :meth:`~dpid.dPID.measured` value.
    * Request a :meth:`~dpid.dPID.result`.
    * Assert the returned value is (almost) equal to the pre-computed number.

* Run ``pytest`` again.

  - It should run both the existing example, and the new test-file.
  - The test should fail! As the *empty* class always returns ``0``, that is easy.
  - Watch for *syntax errors*, and errors but AssertionError. Improve your code when needed

* Repeat, either by adding test-function to that file, or adding more test-files.

  - When needed, you can add auxiliary functions; just don’t use the *test*-phrase in there name.
  - Or continue first with the implementation part. And add more test later (for other functions).
  - Each test should be a little more complicated as the existing onces.
  - Or better: start with the trivial once. Then the almost-trivial, etc.

    * Start testing a “*P-only*” PID-controller
    * Then an “*I-only*”, then a “*D-only*”. After which you test a simple combination
    * etc.

Code second
-----------

When a part of the functionality is tested (or at least: there is test-code for), you can start implementing
the :class:`~dpid.dPID` class. Keep is simple. The only objective is to **make one failing test pass**.

And improve (refactor)
----------------------


