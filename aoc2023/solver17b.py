from heapq import heappush, heappop

def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]


def _get_new_direction(direction):
    for new_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if new_direction != direction and new_direction != (-direction[0], -direction[1]):
            yield new_direction


def get_new_positions(current_pos, direction, length_x, length_y):
    for new_direction in _get_new_direction(direction):
        tmp = current_pos
        path = []
        for i in range(10):
            a, b = tmp = add(tmp, new_direction)
            path.append(tmp)
            if i < 3:
                continue
            if 0 <= a < length_x and 0 <= b < length_y:
                yield (a, b), new_direction, path


def solve(data_in: str):
    space = {}
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            space[(x, y)] = int(char)
    length_x = len(data_in.splitlines()[0])
    length_y = len(data_in.splitlines())
    start = (0, 0)
    end = (length_x - 1, length_y - 1)
    min_map = {}
    stack_to_check = []
    heappush(stack_to_check, (0, start, (-1, -1)))
    total = 2**32
    while stack_to_check:
        cost, pos, direction = heappop(stack_to_check)
        if pos == end:
            total = min(total, cost)
            break
        for new_pos, new_direction, path in get_new_positions(pos, direction, length_x, length_y):
            new_cost = cost + sum([space[p] for p in path])
            if (new_pos, new_direction) not in min_map or min_map[(new_pos, new_direction)] > new_cost:
                min_map[(new_pos, new_direction)] = new_cost
                heappush(stack_to_check, (new_cost, new_pos, new_direction))
    print(total)
    return total
