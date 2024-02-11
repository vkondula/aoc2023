
class Range:
    def __init__(self, start, length, dst_start):
        self.start = start
        self.length = length
        self.offset = dst_start - start

    def __contains__(self, value):
        return self.start <= value < self.start + self.length

    def get(self, value):
        if value in self:
            return value + self.offset
        raise ValueError(f"{value} not in {self}")


def solve(data_in: str):
    categories = data_in.split("\n\n")
    seeds = [int(value) for value in categories[0].split(": ")[1].split(" ")]
    rules: list[list[Range]] = [[] for _ in range(len(categories) - 1)]
    for i, category in enumerate(categories[1:]):
        for row in category.split(":\n")[1].split("\n"):
            dst, src, length = row.split(" ")
            rules[i].append(Range(int(src), int(length), int(dst)))
    min_values = 2**32
    for seed in seeds:
        tmp = seed
        for group in rules:
            for rule in group:
                if tmp in rule:
                    tmp = rule.get(tmp)
                    break
        min_values = min(min_values, tmp)
    print(min_values)
    return min_values
