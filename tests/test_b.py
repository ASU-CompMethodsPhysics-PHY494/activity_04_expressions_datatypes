import pytest

from .tst import _test_variable

def test_b(name='b', reference=['C', 'D']):
    return _test_variable(name, reference, mod="slices.py")

