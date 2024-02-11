def solve(data_in: str):
    total = 0
    for item in data_in.split(","):
        subtotal = 0
        for char in item:
            subtotal += ord(char)
            subtotal *= 17
            subtotal %= 256
        total += subtotal
    print(total)
    return total

