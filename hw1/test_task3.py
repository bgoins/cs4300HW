import pytest
from task3 import ifstruc, primefunc, whilestruc

@pytest.mark.parametrize("input,expected",[(1,"Positive"),(0,"Zero"),(-1,"Negative")])

def test_ifstruc(input,expected):
    assert ifstruc(input) == expected

def test_primefunc():
    expectedprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primefunc() == expectedprimes

def test_whilestruc():
    assert whilestruc() == 5050

