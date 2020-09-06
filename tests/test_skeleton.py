# -*- coding: utf-8 -*-

import pytest
from rt2600ac_py.skeleton import fib

__author__ = "bugbiteme"
__copyright__ = "bugbiteme"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
