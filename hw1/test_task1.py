import pytest
from task1 import hello

def test_hello(capsys):
    hello()
    consolecapture = capsys.readouterr()
    assert consolecapture.out == 'Hello, World!\n'