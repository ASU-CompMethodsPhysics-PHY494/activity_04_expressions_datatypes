import pytest
from .tst import _test_file


@pytest.mark.parametrize("name", ["tempconverter.py", "slices.py", "stuff.py"])
def test_file_exists(name):
    return _test_file(name)
