.. Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017.
   Part of MESS-DocIdeas

.. _pytest_into:

===================
Pytest introduction
===================
:status: Beta


By using pytest_, its becomes simple to run one, several or all test-functions. It has many
advanced features, which are not needed for this exercise; but feel free to visit the website.

Pytest_ uses *autodiscovery* to find all tests. This makes all test-scripts a lot shorter (and easier
to maintain), as the *"main-trick”* isn’t needed in all those files.

Without pytest_ all test-files should have a section like:

.. code-block:: python

   if __name__ == "__main__":
      test_P()
      test_clip()
      ...
      # list ALL your test here!

Effectively, pytest_ will automatically discover all test-functions; and execute them as-if that
section is added, with all test-function listed (in file-order).

Example
=======

.. highlight:: shell-session

* Installation of pytest_ is trivial; use::

    [Albert@pyMESS:] % pip install pytest

* Running all test (in 1 directory) is trivial too::

    [Albert@pyMESS:../dPID] % pytest
    ======================================================== test session starts =========================================================
    platform darwin -- Python 3.4.1, pytest-3.0.4, py-1.4.31, pluggy-0.4.0
    rootdir: /Users/albert/work/MESS-DocIdeas,hg/BureauLade/dPID, inifile:
    collected 2 items

    test_examples.py .F

    ============================================================== FAILURES ==============================================================
    _____________________________________________________________ test_clip ______________________________________________________________

        def test_clip():
            c = dPID(1,2,3)

            c.set_min_max(min_result=10)
            c.set_min_max(max_result=10)

            for sp in range(-100,100,10):
                c.setpoint(sp)
                c.measured(0)

                got = c.result()
    >           assert got == 10, "Both min and max are clipped to 10; so result should be 10!. But it is: %s" % c.result()
    E           AssertionError: Both min and max are clipped to 10; so result should be 10!. But it is: 0.0
    E           assert 0.0 == 10

    test_examples.py:33: AssertionError
    ================================================= 1 failed, 1 passed in 0.09 seconds =================================================

  .. note:: expect *AssertionError*\s (**ONLY**)

     * As the class isn’t implemented, one should expect *Asserts* during those (initial) runs.
     * Make sure you find *AssertionError*\s only; no syntax-errors etc! They denote mistakes in your code!

* The used test-file (test_examples.py) can be found :ref:`here <dPID_test_examples>`

.. _pytest_conventions:

Conventions
===========

To make this (*autodiscovery*) possible, one has to fullfil a few conventions:

#. All (python) files containing test-functions, should start with ``test_``

   * Alternative: end with ``_test.py``

   * Typically, *I* use the prefix for black-box and glass-box tests. And the suffix for white-box tests.

#. All test-functions should have a name starting with ``test_``

   * No other function should *not* use that prefix!

#. Test-functions are called without arguments

   * It possible to define ‘parameter’; they are used as `fixtures
     <https://docs.pytest.org/en/latest/fixture.html?highlight=fixture>`__

   * Those aren’t needed for this exercise. So, define all test-functions without parameters!


OK or NOK: Assert on failure
============================

Every test should result in a single-bit of information: OK nor Not-OK. Sometimes it may be useful
to log (print) intermediate results; that can’t replace the OK/NOK bit however.

With pytest_ this is easy: use the ``assert`` *statement*!

Typically a test ends with an assert. However, it perfectly normal to have many asserts in one
test-function; each one acts as a kind of sub-test. When a test succeeds hardly any output is
generated; preventing cluttering of the tets-reports.

When the first assert-expression results in ``False`` the test Fails. Then that AssertionError is
show with some context. Giving the programmer feedback on which test fails and why.

.. warning:: Assert is NOT a function

   In python ``assert`` is a keyword with one or two expressions.

   Don’t use it as a function; which is a common (starters) mistake. Then, it is read as a single
   expression: a tuple with two elements. Which is always ``True``. So the ``assert`` never fails!

   Typically, the second expression is string explaining what the test expected during this test.

.. _pytest: https://pytest.readthedocs.io/
