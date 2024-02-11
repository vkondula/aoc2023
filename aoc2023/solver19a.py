import re


def get_target(subrule, part):
    test, condition, value, target = subrule
    if condition == "<":
        if part[test] < value:
            return target
    elif condition == ">":
        if part[test] > value:
            return target
    return


def validate_rule(rules, part, rule_name):
    subrules, fallback = rules[rule_name]
    for subrule in subrules:
        target = get_target(subrule, part)
        if target:
            return target
    return fallback


def solve(data_in: str):
    rules_raw, parts_raw = data_in.split("\n\n")
    parts = []
    for row in parts_raw.split("\n"):
        # {x=787,m=2655,a=1222,s=2876}
        parts.append(
            dict(
                zip(
                    ['x', 'm', 'a', 's'],
                    [int(a[0]) for a in re.finditer('\d+', row)]
                )
            )
        )
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
    total = 0
    for part in parts:
        target = "in"
        while True:
            target = validate_rule(rules, part, target)
            if target in ("A", "R"):
                break
        if target == "A":
            total += sum(part.values())
    print(total)
    return total
