CYCLE_COUNT = 1000000000

sort_keys = {
    (0, -1): lambda r: (r[1], r[0]),  # north
    (-1, 0): lambda r: (r[0], r[1]),  # west
    (0, 1): lambda r: (-r[1], r[0]),  # south
    (1, 0): lambda r: (-r[0], r[1]),  # east
}
order = [(0, -1), (-1, 0), (0, 1), (1, 0)]

configurations = {}


def solve(data_in: str):
    rocks = set()
    walls = set()
    width = len(data_in.splitlines()[0])
    length = len(data_in.splitlines())
    for i in range(-1, width + 1):
        walls.add((i, -1))
        walls.add((i, length))
    for j in range(-1, length + 1):
        walls.add((-1, j))
        walls.add((width, j))
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "O":
                rocks.add((x, y))
    i = 0
    moved = False
    while i < CYCLE_COUNT:
        for a, b in order:
            for x, y in sorted(rocks, key=sort_keys[(a, b)]):
                xx, yy = (x + a, y + b)
                while (xx, yy) not in walls and (xx, yy) not in rocks:
                    (xx, yy) = (xx + a, yy + b)
                (xx, yy) = (xx - a, yy - b)
                if (xx, yy) != (x, y):
                    rocks = rocks - {(x, y)}
                    rocks.add((xx, yy))
        configuration = frozenset(rocks)
        if not moved and configuration in configurations:
            past_configuration = configurations[configuration]
            i += (CYCLE_COUNT - i) // (i - past_configuration) * (i - past_configuration)
            moved = True
        configurations[configuration] = i
        i += 1
    total = 0
    for _, y in rocks:
        total += length - y
    print(total)
    return total

def build_map(rocks, walls, width, length) -> list[str]:
    rows = []
    for y in range(length):
        row = []
        for x in range(width):
            if (x, y) in rocks:
                row.append("O")
            elif (x, y) in walls:
                row.append("#")
            else:
                row.append(".")
        rows.append("".join(row))
    return rows


