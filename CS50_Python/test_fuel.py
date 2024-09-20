from fuel import gauge
from fuel import convert


def test_percetage():
    assert convert("3/4") == 75
    assert gauge(75) == "75%"

    assert convert("1/4") == 25
    assert gauge(25) == "25%"

def test_E():
    assert convert("0") == 0
    assert gauge(0) == "E"
    assert convert("1/100") == 1
    assert gauge(1) == "E"


def test_F():
    assert convert("99/100') == 99
    assert gauge(99) == "F"
    assert convert("1") == 100
    assert gauge(1) == "F"

