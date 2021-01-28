import pytest
import importlib
import pathlib
import sys
from io import StringIO


def _test_file(p):
    p = pathlib.Path(p)
    if not p.exists():
        raise AssertionError(f"Solution file '{p}' is missing.")

def _test_variable(name, reference, mod):
    mod = pathlib.Path(mod)
    try:
        module = importlib.import_module(mod.stem)
    except ImportError:
        raise AssertionError(f"Solution file '{mod}' could not be imported")
    try:
        value = getattr(module, name)
    except AttributeError:
        raise AssertionError(f"Solution file '{mod}' does not contain variable '{name}'.")

    try:
        assert value == pytest.approx(reference), f"{name}={value} is not correct"
    except TypeError:
        assert value == reference, f"{name}={value} is not correct"

def _test_variable_with_input(name, input_values, reference, mod):
    mod = pathlib.Path(mod)
    if not mod.exists():
        raise AssertionError(f"Solution file '{mod}' could not be found")

    oldstdin = sys.stdin
    try:
        sys.stdin = StringIO("\n".join([str(s) for s in input_values]) + "\n")
        # main input() reads values
        # execute the code in __main__ and have variables in GLOBALS
        GLOBALS = {'__name__': '__main__'}
        exec(open(mod).read(), GLOBALS)
    finally:
        sys.stdin = oldstdin

    try:
        value = GLOBALS[name]
    except KeyError:
        raise AssertionError(f"Solution file '{mod}' does not contain variable '{name}'.")

    assert value == pytest.approx(reference), f"{name}={value} is not correct"


