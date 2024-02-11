import attr


@attr.s
class PartsRange:
    values: list[tuple[int, int]] = attr.ib()
    mapping = ["x", "m", "a", "s"]

    def split(self, test, condition, value):
        affected_index = self.mapping.index(test)
        affected = self.values[affected_index]
        for new_affected in self.get_affected(affected, condition, value):
            yield PartsRange(
                self.values[:affected_index] + [new_affected] + self.values[affected_index + 1:]
            )

    def get_affected(self, affected, condition, value):
        lt = (affected[0], min(value, affected[1]))
        le = (affected[0], min(value + 1, affected[1]))
        gt = (max(value + 1, affected[0]), affected[1])
        ge = (max(value, affected[0]), affected[1])
        if condition == "<":
            return [lt, ge]
        elif condition == ">":
            return [gt, le]

    def get_combinations(self):
        total = 1
        for values in self.values:
            length = values[1] - values[0]
            total *= length if length > 0 else 0
        return total


def validate_rules(rules, part_range, rule_name):
    total = 0
    if rule_name == "R":
        return 0
    if rule_name == "A":
        return part_range.get_combinations()
    subrules, fallback = rules[rule_name]
    for subrule in subrules:
        test, condition, value, target = subrule
        true_range, part_range = part_range.split(test, condition, value)
        total += validate_rules(rules, true_range, target)
    total += validate_rules(rules, part_range, fallback)
    return total


def solve(data_in: str):
    rules_raw, parts_raw = data_in.split("\n\n")
    rules = {}
    for row in rules_raw.split("\n"):
        # px{a<2006:qkq,m>2090:A,rfg}
        name, rest = row.split("{")
        subrules_raw = rest[:-1].split(",")
        fallback = subrules_raw[-1]
        subrules = []
        for subrule_raw in subrules_raw[:-1]:
            test = subrule_raw[0]
            condition = subrule_raw[1]
            value_raw, target = subrule_raw[2:].split(":")
            value = int(value_raw)
            subrules.append((test, condition, value, target))
        rules[name] = (subrules, fallback)
    total = validate_rules(rules, PartsRange([(1, 4001)] * 4), "in")
    print(total)
    return total
