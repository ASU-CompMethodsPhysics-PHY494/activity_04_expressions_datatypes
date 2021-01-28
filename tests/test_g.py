import pytest

from .tst import _test_variable

def test_g(name='g', reference=[110.0, 101.3, 97.1, 98.8, 78.3, 60.1]):
    return _test_variable(name, reference, mod="slices.py")

