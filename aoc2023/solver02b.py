import re
from collections import defaultdict
from functools import reduce


def solve(data_in: str):
    # format: `Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red`
    total = 0
    for row in data_in.split("\n"):
        game, rounds_raw = row.split(":")
        used = defaultdict(int)
        for round_raw in rounds_raw.split(";"):
            for colour in ["green", "red", "blue"]:
                if match := re.search(r"(\d+) {}".format(colour), round_raw):
                     used[colour] = max(int(match.group(1)), used[colour])
        round = reduce(lambda x, y: x*y, used.values(), 1)
        total += round
    print(total)
    return total
