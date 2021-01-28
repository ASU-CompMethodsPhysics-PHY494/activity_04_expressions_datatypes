import pytest

from .tst import _test_variable

def test_a(name='a', reference='E'):
    return _test_variable(name, reference, mod="slices.py")

