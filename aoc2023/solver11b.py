from itertools import combinations


def solve(data_in: str):
    galaxies = set()
    for y, row in enumerate(data_in.split("\n")):
        for x, char in enumerate(row):
            if char == "#":
                galaxies.add((x,y))
    xl = len(data_in.split("\n")[0])
    yl = len(data_in.split("\n"))
    xs = set(x for (x,y) in galaxies)
    ys = set(y for (x,y) in galaxies)
    xempty = set(range(xl)) - xs
    yempty = set(range(yl)) - ys
    new_galaxies = set()
    for x,y in galaxies:
        new_galaxies.add(
            (
                len([i for i in xempty if i < x]) * (1000000 - 1) + x,
                len([i for i in yempty if i < y]) * (1000000 - 1) + y
            )
        )
    total = 0
    for (x,y), (i,j) in combinations(new_galaxies, 2):
        total += abs(x - i) + abs(y - j)
    print(total)
    return total

