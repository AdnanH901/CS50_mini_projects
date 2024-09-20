import pytest
from working import convert


def test_AM2PM():
    assert convert("11:59 AM to 00:01 PM") == "11:59 to 12:01"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_PM2AM():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_errors1():
    input_str = "9 AM - 5 PM"
    with pytest.raises(ValueError):
        convert(input_str)


def test_errors2():
    input_str = "9:60 AM to 5:60 PM"
    with pytest.raises(ValueError):
        convert(input_str)


def test_errors3():
    input_str = "09:00 AM - 17:00 PM"
    with pytest.raises(ValueError):
        convert(input_str)