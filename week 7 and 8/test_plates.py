from plates import is_valid
import pytest



def test_valid():
    assert is_valid("CS50")==True
    assert is_valid("AAA222") == True
    assert is_valid("ABC") == True

def test_invalid():
    assert is_valid("21AAA")== False
    assert is_valid("A")== False
    assert is_valid("AA22AA") == False
    assert is_valid("AMM!") == False
    assert is_valid("AMM02") == False
    assert is_valid("AB123CD") == False
    assert is_valid("325") == False
    assert is_valid("22CS") == False


