import pytest

from .tst import _test_variable

def test_f(name='f', reference=[101.3, 110.0]):
    return _test_variable(name, reference, mod="slices.py")

