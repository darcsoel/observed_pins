# import pytest
from main import get_pins


def test1():
    input_data = "8"
    expected = ["5", "7", "8", "9", "0"]
    result = get_pins(input_data)
    assert result == expected


def test2():
    input_data = "11"
    expected = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    result = get_pins(input_data)
    assert result == expected
