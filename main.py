from config import BLOCK_SIZE, I_UP_LIMIT, NUMBERS_SCHEMA, I_DOWN_LIMIT, Y_UP_LIMIT, Y_DOWN_LIMIT

NUMBERS = []

for block in NUMBERS_SCHEMA:
    NUMBERS.extend(block)


def find_number_index(number):
    i = NUMBERS.index(number) % BLOCK_SIZE
    y = NUMBERS.index(number) // BLOCK_SIZE
    return y, i


def find_variations(number):
    """Return neighborhoods of number, if exists"""

    y_coordinate, i_coordinate = find_number_index(number)

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

    variations, result = [], []

    for number in observed:
        variations.append(find_variations(number))

    result.extend(variations.pop())

    while variations:
        numbers = variations.pop()
        final = []

        for char in result:
            for number in numbers:
                final.append(f"{number}{char}")

        result = final

    return set(result)
