def solve(data_in: str):
    rocks = set()
    walls = set((x, -1) for x in range(len(data_in.splitlines()[0])))
    length = len(data_in.splitlines())
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "O":
                rocks.add((x, y))
    for i, j in sorted(rocks, key=lambda r: (r[1], r[0])):
        new_j = j
        for new_j in range(j, -1, -1):
            if (i, new_j - 1) in walls or (i, new_j - 1) in rocks:
                break
        if new_j != j:
            rocks = rocks - {(i, j)}
            rocks.add((i, new_j))
    total = 0
    for _, y in rocks:
        total += length - y
    print(total)
    return total

