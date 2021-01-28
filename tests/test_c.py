import pytest

from .tst import _test_variable

def test_c(name='c', reference=['D', 'E']):
    return _test_variable(name, reference, mod="slices.py")

