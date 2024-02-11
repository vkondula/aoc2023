import re
from collections import defaultdict
from functools import reduce


def solve(data_in: str):
    data_in = re.sub(r" +", " ", data_in).split("\n")
    times = [int(a) for a in data_in[0].split(": ")[1].split(" ")]
    distances = [int(a) for a in data_in[1].split(": ")[1].split(" ")]
    beats = defaultdict(int)
    for i, time in enumerate(times):
        for test in range(1, time):
            if (time - test) * test > distances[i]:
                beats[i] += 1
    total = reduce(lambda x, y: x*y, beats.values(), 1)
    print(total)
    return total
