def parse_two_numbers(raw_numbers):
    """
       Utility function to parse input line

       :param str raw_numbers: Space separated numbers. Example: '3 4'
       :return: Parsed two numbers, compacted into list. Example: [3, 4]
       :rtype: list[int, int]
       :raises ValueError: If format of string cannot be parsed into two integer numbers
    """
    try:
        return list(map(int, raw_numbers.split(' ')))
    except Exception:
        raise ValueError('Invalid format. Please check example of usage in the documentation (README.md)')


def find_me(width, height, castle_map):
    """
       Function to find P (starting position) on the map

       :param int width: Width of the map. Example: 6
       :param int height: Height of the map. Example: 26
       :param List[str, ...] castle_map: Castle map. Example: ['##########################', ...]
       :return: Two numbers, which represents x and y coordinates of P. Example: 3, 5
       :rtype: tuple[int, int]
    """
    for i in range(width):
        for j in range(height):
            if castle_map[i][j] == 'P':
                return i, j


def explore_room(p_x, p_y, width, height, castle_map, opened_doors):
    """
       Function to explore the room, assuming that some of the doors can be opened or not
       (depends on opened_doors param). Function will use dfs algorithm to check value of every cell recursively.

       :param int p_x: Position of P (x coordinate), found using find_me function. Example: 5
       :param int p_y: Position of P (x coordinate), found using find_me function. Example: 3
       :param int width: Width of the map. Example: 6
       :param int height: Height of the map. Example: 26
       :param List[str, ...] castle_map: Castle map. Example: ['##########################', ...]
       :param set[tuple[x, y], ...] opened_doors: doors which we assume are opened. Example: {(2, 4), ...}
       :return: Number of keys, coins and doors found in the room. Example:  {'K': 0, 'G': 0, 'D': [(2, 3), ...]}
       :rtype: dict
    """

    def scan_room(x, y):
        """
           Function which is called in recursion to check one cell value and increase statistics saved in visited_cells,
           and room_objects

           :param int x: x coordinate of cell. Example: 5
           :param int y: y coordinate of cell. Example: 3
           :return: Nothing, it update appropriate structures using closure mechanism
           :rtype: None
        """

        cell = castle_map[x][y]
        if visited_cells[x][y] or cell == '#':
            return

        visited_cells[x][y] = True
        if cell in ('G', 'K'):
            room_objects[cell] += 1
        elif (cell == 'D') and ((x, y) not in opened_doors):
            room_objects['D'].append((x, y))
            return

        scan_room(x + 1, y)
        scan_room(x - 1, y)
        scan_room(x, y + 1)
        scan_room(x, y - 1)

    # We can optimize this in future by propagating parent Node parameters to reuse info about already explored cells
    visited_cells = [[0 for _ in range(width)] for _ in range(height)]
    room_objects = {'K': 0, 'G': 0, 'D': []}

    # This is more or less classical search in depth using recursion, to scan all objects in the room
    scan_room(p_x, p_y)
    return room_objects


def find_castle_treasure(width, height, castle_map, opened_doors=None, max_visited_rooms=1,
                         max_found_coins=0, p_x=None, p_y=None):
    """
       Main function to solve the problem. Function do recursive call to build tree and investigate what statistics
       can be gathered depended on which door we decided to open next. Function should return max possible number of
       visited rooms and max possible number of found coins.

       IMPORTANT! We don't have constraint that max collected coins and max visited rooms should
       be found at the same time!

       :param int width: Width of the map. Example: 6
       :param int height: Height of the map. Example: 26
       :param List[str, ...] castle_map: Castle map. Example: ['##########################', ...]
       :param set[tuple[x, y], ...] opened_doors: doors which we assume are opened. Example: {(2, 4), ...}
       :param int max_visited_rooms: Max number of rooms which we visited on current recursive call. Example: 6
       :param int max_found_coins: Max number of coins which we found on current recursive call. Example: 3
       :param int p_x: Position of P (x coordinate), found using find_me function. Example: 5
       :param int p_y: Position of P (x coordinate), found using find_me function. Example: 3
       :param set[tuple[x, y], ...] opened_doors: doors which we assume are opened. Example: {(2, 4), ...}
       :return: subtree, max number of visited rooms, max number of found coins.
       :rtype: tuple[list[dict], int, int]
    """

    # We will build decision tree to find optimal combinations of opened doors which brings max value for us

    if opened_doors is None:  # Let's consider starting point as a root object of our tree
        if opened_doors is None:
            opened_doors = set()
    if (p_x is None) or (p_y is None):
        p_x, p_y = find_me(width, height, castle_map)

    leaf = {
        'stats': None,
        'subtree': [],
        'opened_doors': opened_doors,
    }

    room_stats = explore_room(
        p_x=p_x,
        p_y=p_y,
        width=width,
        height=height,
        castle_map=castle_map,
        opened_doors=leaf['opened_doors']
    )
    leaf['stats'] = room_stats

    # Recursively calculate max number of collected coins
    if leaf['stats']['G'] > max_found_coins:
        max_found_coins = leaf['stats']['G']

    # Recursively calculate max number of visited rooms
    if len(opened_doors) + 1 > max_visited_rooms:
        max_visited_rooms = len(opened_doors) + 1

    leaf['stats']['K'] -= len(opened_doors)  # For each open door we should use a key

    if not leaf['stats']['K'] == 0:  # If we have keys we can use them to open more doors
        for door in leaf['stats']['D']:
            _opened_doors = leaf['opened_doors']
            _opened_doors.add(door)

            # We do recursion to check statistics assuming that some chosen door is open to form our decision tree
            child_leaf, max_visited_rooms, max_found_coins = find_castle_treasure(
                width, height, castle_map, opened_doors=_opened_doors, max_visited_rooms=max_visited_rooms
            )
            child_leaf['subtree'].append(child_leaf)

    return leaf, max_visited_rooms, max_found_coins


# Let's separate input/output logic and domain logic to cover domain logic with tests in another module
if __name__ == '__main__':
    print('Please enter input parameters accordingly to documentation')
    # Read parameters of the map
    height_of_map, width_of_map = parse_two_numbers(input())

    # Loop to read map
    rows = []
    for _ in range(height_of_map):
        row = input()
        rows.append(row)

    # Main function which solves treasure problem
    _, max_num_rooms, max_num_coins = find_castle_treasure(width_of_map, height_of_map, rows)

    print(max_num_rooms)
    print(max_num_coins)
