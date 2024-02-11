
class Range:
    def __init__(self, start, length, *, dst_start=None, offset=None):
        self.start = start
        self.length = length
        self.offset = offset if offset is not None else dst_start - start

    def __contains__(self, value):
        return self.start <= value < self.start + self.length

    def __repr__(self):
        return f"Range({self.start}, {self.end}, {self.offset})"

    @property
    def end(self):
        return self.start + self.length

    def get(self, value):
        if value in self:
            return value + self.offset
        raise ValueError(f"{value} not in {self}")

    def reversed_contains(self, value):
        return self.start + self.offset <= value < self.start + self.offset + self.length

    def reversed_get(self, value):
        if self.reversed_contains(value):
            return value - self.offset
        raise ValueError(f"{value} not in {self}")

    def combine_with(self, others: list["Range"]):
        """Split this range into multiple ranges based on the provided ranges."""
        result = []
        tmp_start = self.start
        for other in others:
            if other.end <= tmp_start:
                continue
            if tmp_start < other.start:
                result.append(Range(tmp_start, other.start - tmp_start, offset=0))
                tmp_start = other.end
            if other.start < self.end:
                result.append(Range(tmp_start + other.offset, min(other.end, self.end) - tmp_start, offset=0))
                tmp_start = min(other.end, self.end)
            if tmp_start not in self:
                break
        if tmp_start < self.end:
            result.append(Range(tmp_start, self.end - tmp_start, offset=0))
        return [r for r in result if r.length > 0]


def solve(data_in: str):
    categories = data_in.split("\n\n")
    tmp_seeds = [int(value) for value in categories[0].split(": ")[1].split(" ")]
    seeds = []
    seed_ranges = []
    for i in range(0, len(tmp_seeds), 2):
        seed_range = Range(tmp_seeds[i], tmp_seeds[i + 1], offset=0)
        seed_ranges.append(seed_range)
        seeds += [seed_range.start, seed_range.end]
    rules: list[list[Range]] = [[] for _ in range(len(categories) - 1)]
    for i, category in enumerate(categories[1:]):
        for row in category.split(":\n")[1].split("\n"):
            dst, src, length = row.split(" ")
            rules[i].append(Range(int(src), int(length), dst_start=int(dst)))
        rules[i] = sorted(rules[i], key=lambda x: x.start)
    current_ranges = seed_ranges
    next_ranges = []
    for group in rules:
        for tmp_range in current_ranges:
            next_ranges += tmp_range.combine_with(group)
        current_ranges = next_ranges
        next_ranges = []
    finals = [r.start for r in current_ranges]
    print(min(finals))
    return min(finals)
