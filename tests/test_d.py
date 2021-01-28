import pytest

from .tst import _test_variable

def test_d(name='d', reference=6):
    return _test_variable(name, reference, mod="slices.py")

