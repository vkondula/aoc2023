import math
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
    current = [a for a in left.keys() if a[2] == "A"]
    first_time = [0 for _ in current]
    while not all(first_time):
        d = next(direction)
        total += 1
        for i, c in enumerate(current):
            if d == "L":
                current[i] = left[c]
            elif d == "R":
                current[i] = right[c]
            if current[i][2] == "Z":
                if first_time[i] == 0:
                    first_time[i] = total
    final = math.lcm(*first_time)
    print(final)
    return final
