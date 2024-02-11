class Pipe:
    def __init__(self, north: int, east: int, south: int, west: int):
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def get_vectors(self):
        if self.north:
            yield (0, -1)
        if self.east:
            yield (1, 0)
        if self.south:
            yield (0, 1)
        if self.west:
            yield (-1, 0)

    def __repr__(self):
        return f"Pipe(north={self.north}, east={self.east}, south={self.south}, west={self.west})"

    def connects(self, location: tuple[int, int]):
        return [
            (location[0] + vector[0], location[1] + vector[1])
            for vector in self.get_vectors()
        ]


pipes = {
    "|": Pipe(1, 0, 1, 0),
    "-": Pipe(0, 1, 0, 1),
    "L": Pipe(1, 1, 0, 0),
    "J": Pipe(1, 0, 0, 1),
    "7": Pipe(0, 0, 1, 1),
    "F": Pipe(0, 1, 1, 0),
    "S": Pipe(0, 0, 0, 0),
}

filler = {
    (0, 1): "|",
    (1, 0): "-",
    (0, -1): "|",
    (-1, 0): "-",
}


def get_distance_map(pipes_map: dict[tuple[int, int], Pipe], start: tuple[int, int]):
    queue = []
    distance_map = {}
    for i in range(-1, 2):
        for j in range(-1, 2):
            loc = (start[0] + i, start[1] + j)
            if loc in pipes_map and start in pipes_map[loc].connects(loc):
                queue.append(loc)
                distance_map[loc] = 1
    while queue:
        current = queue.pop(0)
        distance = distance_map[current]
        if current not in pipes_map:
            continue
        for next_ in pipes_map[current].connects(current):
            if next_ not in distance_map:
                distance_map[next_] = distance + 1
                queue.append(next_)
    return set(distance_map.keys()) | {start}


def solve(data_in: str):
    start = None
    pipes_map = {}
    extended_map = {}
    for y, line in enumerate(data_in.split("\n")):
        for x, char in enumerate(line):
            if char in pipes:
                pipes_map[(x, y)] = pipes[char]
            if char == "S":
                start = (x, y)
    for (a, b) in get_distance_map(pipes_map, start):
        extended_map[(a * 2, b * 2)] = pipes_map[(a, b)]

    queue = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            (a,b) = (start[0] + i, start[1] + j)
            if (a,b) in pipes_map and start in pipes_map[(a,b)].connects((a,b)):
                queue.append((a*2,b*2))
    handled = set()
    # extend to 2 times the size, then connect pipes
    while queue:
        loc = queue.pop(0)
        handled.add(loc)
        for vector in extended_map[loc].get_vectors():
            if vector in filler:
                tmp_loc = (loc[0] + vector[0], loc[1] + vector[1])
                if tmp_loc not in extended_map:
                    extended_map[tmp_loc] = pipes[filler[vector]]
                for vector2 in extended_map[tmp_loc].get_vectors():
                    new_loc = (tmp_loc[0] + vector2[0], tmp_loc[1] + vector2[1])
                    if new_loc not in handled:
                        queue.append(new_loc)
    # flood fill from -1,-1
    queue = {(-1, -1),}
    handled = set()
    y_range = range(-1, len(data_in.split("\n")) * 2 + 3)
    x_range = range(-1, len(data_in.split("\n")[0]) * 2 + 3)
    while queue:
        current = queue.pop()
        handled.add(current)
        for i in range(-1, 2):
            for j in range(-1, 2):
                loc = (current[0] + i, current[1] + j)
                if loc not in handled and loc not in extended_map and loc[0] in x_range and loc[1] in y_range:
                    queue.add(loc)

    outside_unified = {(a//2, b//2) for a,b in handled if not a % 2 and not b % 2}
    unified_pipes = {(a//2,b//2) for a,b in extended_map.keys() if not a % 2 and not b % 2}
    total_map = {(a,b) for a in range(len(data_in.split("\n")[0])) for b in range(len(data_in.split("\n")))}
    return len(total_map - outside_unified - unified_pipes)
