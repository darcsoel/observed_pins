from main import get_pins, find_number_index, find_variations


def test1():
    input_data = "8"
    expected = ["5", "7", "8", "9", "0"]
    result = get_pins(input_data)
    assert not set(result) ^ set(expected)


def test2():
    input_data = "11"
    expected = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    result = get_pins(input_data)
    assert not set(result) ^ set(expected)


def test_index_find_1():
    number = "1"
    i_coordinate, y_coordinate = find_number_index(number)
    assert i_coordinate == 0
    assert y_coordinate == 0


def test_index_find_2():
    number = "2"
    i_coordinate, y_coordinate = find_number_index(number)
    assert i_coordinate == 1
    assert y_coordinate == 0


def test_index_find_4():
    number = "4"
    i_coordinate, y_coordinate = find_number_index(number)
    assert i_coordinate == 0
    assert y_coordinate == 1


def test_variations_1():
    input_data = "1"
    expected = ["1", "2", "4"]
    variations = find_variations(input_data)
    assert not set(variations) ^ set(expected)


def test_variations_8():
    input_data = "8"
    expected = ["5", "7", "8", "9", "0"]
    variations = find_variations(input_data)
    assert not set(variations) ^ set(expected)
