import pytest

from .tst import _test_variable_with_input

refT = lambda x: 273.15 + (x - 32.0) * 5/9

@pytest.mark.parametrize("theta", [32.0, 100, -40.1, 1000])
def test_T_Kelvin(theta):
    return _test_variable_with_input('T', [theta], refT(theta), mod="tempconverter.py")


