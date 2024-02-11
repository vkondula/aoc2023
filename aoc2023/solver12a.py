CACHE = {}


def get_valid_rows_count(row: str, damaged_map: list[int]) -> int:
    if not damaged_map:
        return 1 if "#" not in row else 0
    if (row, tuple(damaged_map)) in CACHE:
        return CACHE[(row, tuple(damaged_map))]
    current = damaged_map[0]
    total = 0
    for i in range(len(row)):
        if i + current >= len(row):
            break
        if i and row[i - 1] == "#":
            break
        for j in range(current):
            if row[i + j] == ".":
                break
        else:
            if row[i + current] != "#":
                tmp = get_valid_rows_count(row[i + current + 1:], damaged_map[1:])
                total += tmp
                CACHE[(row[i + current + 1:], tuple(damaged_map[1:]))] = tmp
    return total


def solve(data_in: str):
    total = 0
    for row_raw in data_in.split("\n"):
        row, data = row_raw.split(" ")
        row += "."
        damaged_map = [int(a) for a in data.split(",")]
        total += get_valid_rows_count(row, damaged_map)
    print(total)
    return total



