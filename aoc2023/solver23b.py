from collections import defaultdict


def solve(data_in: str):
    # parse
    spaces = set()
    walls = set()
    start = (1, 0)
    max_y = len(data_in.splitlines()) - 1
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            else:
                spaces.add((x, y))
    # build graph
    nodes = {start}
    visited = {start}
    stack = [((1, 1), 1, start)]
    nodes_mapping = defaultdict(int)
    neighbors = defaultdict(set)
    while stack:
        pos, length, last_node = stack.pop()
        to_visit = set()
        visited.add(pos)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos in walls or new_pos == last_node or (new_pos in visited and new_pos not in nodes):
                continue
            if new_pos in spaces:
                to_visit.add(new_pos)
                continue
        if len(to_visit) > 1 or pos[1] == max_y or pos in nodes:
            key = tuple(sorted([last_node, pos]))
            nodes_mapping[key] = max(length, nodes_mapping[key])
            neighbors[last_node].add(pos)
            neighbors[pos].add(last_node)
            last_node = pos
            length = 0
            nodes.add(pos)
        for new_pos in to_visit:
            stack.append((new_pos, length + 1, last_node))
            continue
    # traverse graph
    total = 0
    stack = [(start, 0, {start})]
    while stack:
        pos, length, path = stack.pop()
        if pos[1] == max_y:
            total = max(total, length)
            continue
        for neighbor in neighbors[pos]:
            if neighbor in path:
                continue
            new_path = path | {neighbor}
            key = tuple(sorted([pos, neighbor]))
            stack.append((neighbor, length + nodes_mapping[key], new_path))
    print(total)
    return total

