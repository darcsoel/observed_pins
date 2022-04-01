from config import BLOCK_SIZE, I_UP_LIMIT, NUMBERS_SCHEMA, I_DOWN_LIMIT, Y_UP_LIMIT, Y_DOWN_LIMIT


def find_number_index(number):
    """Return i,y coordinates of number, based on phone-numbers matrix"""

    try:
        number = int(number)
    except TypeError:
        return None, None

    i = (number % BLOCK_SIZE) - 1
    y = number // BLOCK_SIZE

    return i, y


def find_variations(number):
    """Return neighborhoods of number, if exists"""

    i_coordinate, y_coordinate = find_number_index(number)

    if i_coordinate is None:
        return []

    if i_coordinate == I_UP_LIMIT:
        left = None
    else:
        left = NUMBERS_SCHEMA[y_coordinate][i_coordinate - 1]

    if i_coordinate == I_DOWN_LIMIT:
        right = None
    else:
        right = NUMBERS_SCHEMA[y_coordinate][i_coordinate + 1]

    if y_coordinate == Y_UP_LIMIT:
        up = None
    else:
        up = NUMBERS_SCHEMA[y_coordinate - 1][i_coordinate]

    if y_coordinate == Y_DOWN_LIMIT:
        down = None
    else:
        down = NUMBERS_SCHEMA[y_coordinate + 1][i_coordinate]

    return [x for x in [left, right, up, down, number] if x]


def get_pins(observed):
    """Return all combinations"""

    result = []

    for number in observed:
        pass

    return result
