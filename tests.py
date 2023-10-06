from castle_treasure import find_castle_treasure

ERROR_MESSAGE = 'Assertion failed for {case} case. Expected: {expected}, actual: {actual}'


def test_1_from_description():
    height_of_map = 6
    width_of_map = 26
    rows = [
        '##########################',
        '#................G.......#',
        '#...P....................#',
        '#.............G........G.#',
        '#.................G......#',
        '##########################'
    ]

    case = '1 from description'
    expected_max_num_rooms = 1
    expected_max_num_coins = 4

    _, max_num_rooms, max_num_coins = find_castle_treasure(width_of_map, height_of_map, rows)

    assert max_num_rooms == expected_max_num_rooms, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_rooms,
        actual=max_num_rooms
    )

    assert max_num_coins == expected_max_num_coins, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_coins,
        actual=max_num_coins
    )


def test_2_from_description():
    width_of_map = 26
    height_of_map = 6
    rows = [
        '##########################',
        '#.................#......#',
        '#...P.............D......#',
        '#.................#....G.#',
        '#.K...............#......#',
        '##########################'
    ]

    case = '2 from description'
    expected_max_num_rooms = 2
    expected_max_num_coins = 1

    _, max_num_rooms, max_num_coins = find_castle_treasure(width_of_map, height_of_map, rows)

    assert max_num_rooms == expected_max_num_rooms, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_rooms,
        actual=max_num_rooms
    )

    assert max_num_coins == expected_max_num_coins, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_coins,
        actual=max_num_coins
    )


def test_3_from_description():
    height_of_map = 13
    width_of_map = 26
    rows = [
        '##########################',
        '#.G..#.......#.......G...#',
        '#....D.......D.....G....K#',
        '######.......#############',
        '#....#...................#',
        '#..P.#...G.......K..K....#',
        '#....#...................#',
        '#######D##################',
        '#.G.........#............#',
        '#...........#............#',
        '#...........D..........GG#',
        '#.K.........#..........GG#',
        '##########################'
    ]

    case = '3 from description'
    expected_max_num_rooms = 1
    expected_max_num_coins = 0

    _, max_num_rooms, max_num_coins = find_castle_treasure(width_of_map, height_of_map, rows)

    assert max_num_rooms == expected_max_num_rooms, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_rooms,
        actual=max_num_rooms
    )

    assert max_num_coins == expected_max_num_coins, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_coins,
        actual=max_num_coins
    )


def test_4_from_description():
    height_of_map = 13
    width_of_map = 26
    rows = [
        '##########################',
        '#.G..#.......#.......G...#',
        '#....D.......D.....G....K#',
        '######.......#############',
        '#........................#',
        '#..P.....G.......K..K....#',
        '#........................#',
        '#######D##################',
        '#.G.........#............#',
        '#...........#............#',
        '#...........D..........GG#',
        '#.K.........#..........GG#',
        '##########################'
    ]

    case = '4 from description'
    expected_max_num_rooms = 5
    expected_max_num_coins = 9  # Original description contains wrong value!!!

    _, max_num_rooms, max_num_coins = find_castle_treasure(width_of_map, height_of_map, rows)

    assert max_num_rooms == expected_max_num_rooms, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_rooms,
        actual=max_num_rooms
    )

    assert max_num_coins == expected_max_num_coins, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_coins,
        actual=max_num_coins
    )


def test_keys_more_than_doors():
    width_of_map = 13
    height_of_map = 26
    rows = [
        '##########################',
        '#.G..#.......#.......G...#',
        '#....D.......D.....G....K#',
        '######...K...#############',
        '#........................#',
        '#..P.....G...K...K..K....#',
        '#........................#',
        '#######D##################',
        '#.G.........#............#',
        '#...........#............#',
        '#...........D..........GG#',
        '#.K.........#..........GG#',
        '##########################'
    ]

    case = 'keys more than doors'
    expected_max_num_rooms = 5
    expected_max_num_coins = 9

    _, max_num_rooms, max_num_coins = find_castle_treasure(height_of_map, width_of_map, rows)

    assert max_num_rooms == expected_max_num_rooms, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_rooms,
        actual=max_num_rooms
    )

    assert max_num_coins == expected_max_num_coins, ERROR_MESSAGE.format(
        case=case,
        expected=expected_max_num_coins,
        actual=max_num_coins
    )


if __name__ == '__main__':
    test_1_from_description()
    test_2_from_description()
    test_3_from_description()
    test_4_from_description()
    test_keys_more_than_doors()
