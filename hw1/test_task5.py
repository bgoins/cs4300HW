import pytest
from task5 import books, students

def test_books():
    slicedlisttest = ["Eragon, Chris Paolini", "Metamorphasis, Franz Kafa", "Deltora, Emily Rodda"]
    assert books() == slicedlisttest

def test_students():
    studicttest = {"Alpha":101,"Beta":202, "Delta":303}
    assert students() == studicttest
