import pytest

from .tst import _test_variable

def test_e(name='e', reference=101.3):
    return _test_variable(name, reference, mod="slices.py")

