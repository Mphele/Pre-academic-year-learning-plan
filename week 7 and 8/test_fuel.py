from fuel import convert , gauge
import pytest


def test_convert():
    assert convert("1/4")==25
    assert convert("2/3")==67
    assert convert("0/10")==0

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(73) == "73%"

def test_convert_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/")
    with pytest.raises(ValueError):
        convert("/4")
    # with pytest.raises(ValueError):
    #     convert("3/-4")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
