from itertools import cycle


def solve(data_in: str):
    direc, map_row = data_in.split("\n\n")
    left = {}
    right = {}
    for row in map_row.split("\n"):
        start, other = row.split(" = ")
        l, r = other.strip("(").strip(")").split(", ")
        left[start] = l
        right[start] = r
    direction = cycle(direc)
    total = 0
    current = "AAA"
    while current != "ZZZ":
        d = next(direction)
        if d == "L":
            current = left[current]
        elif d == "R":
            current = right[current]
        total += 1
    print(total)
    return total