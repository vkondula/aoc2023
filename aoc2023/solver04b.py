def solve(data_in: str):
    data = data_in.split("\n")
    rows_count_mapping = {i: 1 for i, _ in enumerate(data, start=1)}
    for i, row in enumerate(data, start=1):
        winning_seq, guesses_seq = row.split(": ")[1].split(" | ")
        winning = set(int(a.strip()) for a in winning_seq.split(" ") if a.strip())
        matches = 0
        for guess in guesses_seq.split(" "):
            if guess and int(guess.strip()) in winning:
                matches += 1
        for j in range(1, matches + 1):
            rows_count_mapping[i + j] += rows_count_mapping[i]
    total = sum(rows_count_mapping.values())
    print(total)
    return total
