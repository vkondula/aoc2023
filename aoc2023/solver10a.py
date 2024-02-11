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
}


def solve(data_in: str):
    start = None
    pipes_map = {}
    for y, line in enumerate(data_in.split("\n")):
        for x, char in enumerate(line):
            if char in pipes:
                pipes_map[(x, y)] = pipes[char]
            if char == "S":
                start = (x, y)
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
    final = max(distance_map.values())
    print(final)
    return final
