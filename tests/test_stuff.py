import pytest

from .tst import _test_variable

def test_stuff(name='stuff', reference=['dog', 42, -1.234, 'cat', [3, 2, 1]]):
    return _test_variable(name, reference, mod="stuff.py")


