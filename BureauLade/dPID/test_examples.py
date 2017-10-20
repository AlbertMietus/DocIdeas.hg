# Copyright (C) 2017: ALbert Mietus, -*- coding: utf-8 -*-
# Dropjes licencie: Beloon me met dropjes naar nuttigheid

import pytest

from logging import getLogger
logger = getLogger(__name__)

from dpid import dPID

def test_P():
    MARGIN  = 0.5

    c = dPID(1,0,0)

    c.setpoint(10.0)
    c.measured(10.0)
    out = c.result()

    assert (-1*MARGIN) < out < MARGIN, "result (%s) should be close to zero (MARGIN=%s)" % (out, MARGIN)

def test_clip():
    c = dPID(1,2,3)

    c.set_min_max(min_result=10)
    c.set_min_max(max_result=10)

    for sp in range(-100,100,10):
        c.setpoint(sp)
        c.measured(0)

        got = c.result()
        assert got == 10, "Both min and max are clipped to 10; so result should be 10!. But it is: %s" % c.result()
