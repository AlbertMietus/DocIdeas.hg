.. Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2017.
   Part of MESS-DocIdeas

====================
dPID: The dPID class
====================
:status: RC-1.0

This articles shows the :class:`dpid.PID` documentation, as specified in :ref:`the python file
<dPID_code>`.

It specifies the *interface* the discrete-PID-controller. Study it to understand how the
class should be used. Then start writing python code to test it.

.. attention:: Its’ a **python-coding** exercise

   When part of this controller is 100% clear, just assume it is working correctly. And fill in the
   details as needed. Use that as base for your test-code.

   * At least, eventually, the class and the code are consistent. So, future changes will not
     invalidate current (assumed) behaviour; without notice.
   * During normal development, such details should be incorporated into the doc-string; possible
     after discussion and/or approval
   * For the ‘homework-goal’ the exact working isn’t that relevant. Fill in details as needed;
     **focus on writing python-code**!


.. autoclass:: dpid.dPID
    :members:

