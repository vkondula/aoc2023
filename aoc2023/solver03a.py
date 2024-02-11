import re


def get_number_and_borders(match: re.Match, row_number: int):
    return int(match.group(0)),  set(
        (i, j)
        for i in range(row_number - 1, row_number + 2)
        for j in range(match.start() - 1, match.end() + 1)
    )


def solve(data_in: str):
    mapping = list()
    symbols = set()
    for i, row in enumerate(data_in.split("\n")):
        for match in re.finditer(r"(\d+)", row):
            mapping.append(get_number_and_borders(match, i))
        for j, value in enumerate(row):
            if not value.isdigit() and value != ".":
                symbols.add((i,j))
    total = 0
    for number, borders in mapping:
        if borders & symbols:
            total += number
    print(total)
    return total
