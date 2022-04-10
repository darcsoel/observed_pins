from main import get_pins, find_number_index, find_variations


def test1():
    input_data = "8"
    expected = ["5", "7", "8", "9", "0"]
    result = get_pins(input_data)
    assert not result ^ set(expected)


def test2():
    input_data = "11"
    expected = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
    result = get_pins(input_data)
    assert not result ^ set(expected)


def test3():
    input_data = "369"
    expected = [
        "236",
        "238",
        "239",
        "256",
        "258",
        "259",
        "266",
        "268",
        "269",
        "296",
        "298",
        "299",
        "336",
        "338",
        "339",
        "356",
        "358",
        "359",
        "366",
        "368",
        "369",
        "396",
        "398",
        "399",
        "636",
        "638",
        "639",
        "656",
        "658",
        "659",
        "666",
        "668",
        "669",
        "696",
        "698",
        "699",
    ]
    result = get_pins(input_data)
    assert not result ^ set(expected)


def test_index_find_1():
    number = "1"
    y_coordinate, i_coordinate = find_number_index(number)
    assert y_coordinate == 0
    assert y_coordinate == 0


def test_index_find_2():
    number = "2"
    y_coordinate, i_coordinate = find_number_index(number)
    assert y_coordinate == 0
    assert i_coordinate == 1


def test_index_find_3():
    number = "3"
    y_coordinate, i_coordinate = find_number_index(number)
    assert y_coordinate == 0
    assert i_coordinate == 2


def test_index_find_4():
    number = "4"
    y_coordinate, i_coordinate = find_number_index(number)
    assert y_coordinate == 1
    assert i_coordinate == 0


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
