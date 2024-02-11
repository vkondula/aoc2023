def solve(data_in: str):
    data = data_in.split("\n")
    total = 0
    for row in data:
        for i in row:
            a, b = "", ""
            if i.isdigit():
                a = i
                break
        for i in row[::-1]:
            if i.isdigit():
                b = i
                break
        total += int(a+b)
    print(total)
    return total
