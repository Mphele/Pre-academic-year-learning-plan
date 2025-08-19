from bank import value
import pytest


def test_hello():
    assert value("hello")==0
    assert value("Hello")==0

def test_h():
    assert value("home")==20
    assert value("Home")==20

def test_no_h():
    assert value("orange")==100

def test_nostart_h():
    assert value("What")==100

# def test_not_capital():
#     assert value("H")==100
