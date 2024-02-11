from collections import defaultdict

slopes_mapping = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}
reversed_slopes_mapping = {a: b for b, a in slopes_mapping.items()}


def solve(data_in: str):
    spaces = set()
    walls = set()
    slopes = defaultdict(set)
    start = (1, 0)
    for x, line in enumerate(data_in.splitlines()):
        for y, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == ".":
                spaces.add((x, y))
            else:
                slopes[char].add((x, y))
    stack = [(start, 0, set())]
    total = 0
    while stack:
        pos, length, path = stack.pop()
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos in walls or new_pos in path:
                continue
            if new_pos in spaces or new_pos in slopes[reversed_slopes_mapping[direction]]:
                new_path = path | {new_pos}
                stack.append((new_pos, length + 1, new_path))
                continue
            total = max(total, length)
    print(total)
    return total

