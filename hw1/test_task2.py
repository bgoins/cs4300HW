# test_task2.py
import pytest
from task2 import integerfunc, floatfunc, stringfunc, booleanfunc

def test_integerfunc():
    assert isinstance(integerfunc(), int)

def test_floatfunc():
    assert isinstance(floatfunc(), float)

def test_stringfunc():
    assert isinstance(stringfunc(), str)

def test_booleanfunc():
    assert isinstance(booleanfunc(), bool)
