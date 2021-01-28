import pytest

from .tst import _test_variable

def test_g(name='g', reference=['F', 'E', 'D', 'C', 'B', 'A']):
    return _test_variable(name, reference, mod="slices.py")

