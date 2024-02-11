def solve(data_in: str):
    data = data_in.split("\n")
    total = 0
    for row in data:
        winning_seq, guesses_seq = row.split(": ")[1].split(" | ")
        winning = set(int(a.strip()) for a in winning_seq.split(" ") if a.strip())
        matches = 0
        for guess in guesses_seq.split(" "):
            if guess and int(guess.strip()) in winning:
                matches += 1
        if matches:
            total += 2 ** (matches - 1)
    print(total)
    return total
