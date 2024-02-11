def get_next_row(row):
    return [
        row[i] - row[i - 1]
        for i in range(1, len(row))
    ]


def all_zero(row):
    return all(a == 0 for a in row)


def solve(data_in: str):
    data = [
        [int(a) for a in row.split(" ")]
        for row in data_in.split("\n")
    ]
    total = 0
    for row in data:
        stack = []
        current = row
        while not all_zero(current):
            stack.append(current)
            next_row = get_next_row(current)
            current = next_row
        predicted = 0
        while stack:
            predicted = stack.pop()[-1] + predicted
        total += predicted
    print(total)
    return total

