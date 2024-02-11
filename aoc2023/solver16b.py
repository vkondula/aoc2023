def add(vector, direction, max_x, max_y):
    new_vector = (vector[0] + direction[0], vector[1] + direction[1])
    if new_vector[0] < 0 or new_vector[0] >= max_x or new_vector[1] < 0 or new_vector[1] >= max_y:
        return None
    return new_vector


next_turns = {
    "|": {
        (1,0): {(0, 1), (0, -1)},
        (-1,0): {(0, 1), (0, -1)},
        (0,1): {(0, 1)},
        (0,-1): {(0, -1)},
    },
    "-": {
        (0, 1): {(1, 0), (-1, 0)},
        (0, -1): {(1, 0), (-1, 0)},
        (1, 0): {(1, 0)},
        (-1, 0): {(-1, 0)},
    },
    "/": {
        (1,0): {(0, -1)},
        (-1,0): {(0, 1)},
        (0,1): {(-1, 0)},
        (0,-1): {(1, 0)},
    },
    "\\": {
        (1,0): {(0, 1)},
        (-1,0): {(0, -1)},
        (0,1): {(1, 0)},
        (0,-1): {(-1, 0)},
    },
    ".": {
        (1,0): {(1, 0)},
        (-1,0): {(-1, 0)},
        (0,1): {(0, 1)},
        (0,-1): {(0, -1)},
    }
}


def solve(data_in: str):
    space = {}
    for y, line in enumerate(data_in.split("\n")):
        for x, char in enumerate(line):
            space[(x,y)] = char
    max_x = len(data_in.split("\n")[0])
    max_y = len(data_in.split("\n"))
    starting_combination = [
        ((i,0), (0,1)) for i in range(max_x)
    ] + [
        ((i,max_y-1), (0,-1)) for i in range(max_x)
    ] + [
        ((0,i), (1,0)) for i in range(max_y)
    ] + [
        ((max_x-1,i), (-1,0)) for i in range(max_y)
    ]
    total = 0
    for beam, direction in starting_combination:
        energized = set()
        stack = [(beam, direction)]
        handled = set()
        while stack:
            beam, direction = stack.pop()
            energized.add(beam)
            handled.add((beam, direction))
            new_directions = next_turns[space[beam]][direction]
            for new_direction in new_directions:
                if new_beam := add(beam, new_direction, max_x, max_y):
                    if (new_beam, new_direction) not in handled:
                        stack.append((new_beam, new_direction))
        total = max(len(energized), total)
    print(total)
    return total


