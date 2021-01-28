import pytest

from .tst import _test_variable

def test_f(name='f', reference=['E', 'F']):
    return _test_variable(name, reference, mod="slices.py")

