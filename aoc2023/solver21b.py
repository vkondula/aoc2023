def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


def normalize_vector(vector, max_x, max_y):
    return vector[0] % max_x, vector[1] % max_y


def solve(data_in: str):
    space = set()
    start = (0, 0)
    max_x = len(data_in.splitlines()[0])
    max_y = len(data_in.splitlines())
    total_steps = 26501365 if max_x > 20 else 5000
    index_start = total_steps % max_x
    snapshots = {index_start + max_x * a: None for a in range(3)}
    for y, line in enumerate(data_in.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                space.add((x, y))
            if char == "S":
                start = (x, y)
    previous = {start}
    current = set()
    i = 0
    while True:
        i += 1
        for x, y in previous:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_pos = (x + dx, y + dy)
                if normalize_vector(new_pos, max_x, max_y) not in space:
                    current.add(new_pos)
        previous = current
        current = set()
        if i in snapshots:
            snapshots[i] = len(previous)
            if all(snapshots.values()):
                break
    total = int(lagrange_interpolation(list(snapshots.keys()), list(snapshots.values()), total_steps))
    print(total)
    return total
