def solve(data_in: str):
    space = set()
    start = (0, 0)
    max_steps = 6 if len(data_in.splitlines()) < 15 else 64
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                space.add((x, y))
            if char == "S":
                start = (x, y)
    previous = {start}
    current = set()
    for _ in range(max_steps):
        for x, y in previous:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_pos = (x + dx, y + dy)
                if new_pos not in space:
                    current.add(new_pos)
        previous = current
        current = set()
    print(len(previous))
    return len(previous)
