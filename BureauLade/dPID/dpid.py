# Copyright (C) 2017: ALbert Mietus, -*- coding: utf-8 -*-
# Dropjes licencie: Beloon me met dropjes naar nuttigheid


from logging import getLogger
logger = getLogger(__name__)

class dPID:
    """A simple discrete-PID controller, as an exercise.

    This PID-controller can be initialised with constantes for P,I and D;
    which can't be changed afterwards.  Optional, a minimum and maximum
    output value can be given; both duration initialisation, and later.

    The controller has two **inputs**: :meth:`.setpoint` and
    :meth:`.measured`, and one **output**: :meth:`.result`. Those inputs can
    be set/updated independently. Similarly, the :meth:`.result` can be read
    at any-moment. As the controller will *remember* the timestamp a values
    changes (and knows when the result is read), it will always give the
    correct output. Thus, that output value does depend on the timestamp it
    is requested!

    The :meth:`.setpoint` is considered as a step-function: between two
    changes, it will remain the last value. The :meth:`.measured` value
    however should be considered as a continues linear-changing value. So,
    between two updates of this value, the dPID-controller will interpolate
    linearly.

    When a :meth:`.result` is read during such a period; the PID-controller can't
    predict the next-measured-value, however. Therefor, it will (for that
    single read) assume the measured-value is the same as last-time.

    When a maximum and/or minimum value is set, the :meth:`.result` will be
    clipped to that value when needed. Without a min/max, the :meth:`.result` is
    unlimited.


    .. hint:: As this class is part of an exercise; no implementation is given.

       One should (after writing the test-functions; and when addressed by
       the trainer) will in the implementation, without(!) changing the
       interface!

       All (numeric) input & output values are either integers or floats.

    """



    def __init__(self, P,I,D, min_result=None, max_result=None): pass

    def setpoint(self, sp):
        """Set the setpoint: a numeric value."""

    def measured(self, value):
        """Give the controller an update on the actual *measured* (or simulated) process-value.

        The controller will assume a linear progression between the last update and the current one
        """

    def result(self):
        """Return the actual result value"""
        return 0.0 # XXX

    def set_min_max(self, min_result=None, max_result=None):
        """Change the minimum and/or maximal result value. Used to clip the :meth:`.result`"""
