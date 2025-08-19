import pytest
from twttr import shorten

def test_shorten():
    assert shorten("twitter")=="twttr"
    assert shorten("tAMmiTha")=="tMmTh"
    assert shorten("twi, t'ter")=="tw, t'tr"
    assert shorten("twitter111")=="twttr111"

def test_error():
    with pytest.raises(TypeError, match="'int' object is not iterable"):
        shorten(23)