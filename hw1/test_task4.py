import pytest
from task4 import calculate_discount

@pytest.mark.parametrize("price,discount,expected",[(100,20,80),(50,30,35),(19.95,15,16.96)])

def test_calculate_discount(price,discount,expected):
    assert calculate_discount(price,discount) == expected

