lookup = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
reversed_lookup = [a[::-1] for a in lookup]


def find_number(row: str, lookup_list: list):
    found = []
    for i, a in enumerate(row):
        if a.isdigit():
            found.append((i, int(a)))
            break
    for i, word in enumerate(lookup_list, start=1):
         if word in row:
              found.append((row.index(word), i))
    return min(found, key=lambda x: x[0])[1]


def solve(data_in: str):
    data = data_in.split("\n")
    total = 0
    for row in data:
        a = find_number(row, lookup)
        b = find_number(row[::-1], reversed_lookup)
        total += int(str(a) + str(b))
    print(total)
    return total
