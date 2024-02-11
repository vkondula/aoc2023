from collections import Counter

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def value(cards):
    en = Counter(cards)
    main = 0
    if 5 in en.values():
        main = 600
    elif 4 in en.values():
        main = 500
    elif 3 in en.values() and 2 in en.values():
        main = 400
    elif 3 in en.values():
        main = 300
    elif [1, 2, 2] == sorted(en.values()):
        main = 200
    elif 2 in en.values():
        main = 100
    # elif card := min(en.keys(), key=lambda x: CARDS.index(x)):
    #     main = 13 - CARDS.index(card)
    return [main] + [13 - CARDS.index(c) for c in cards]


def solve(data_in: str):
    games = []
    for row in data_in.split("\n"):
        cards_row, bet_row = row.split(" ")
        games.append((value(cards_row), int(bet_row), cards_row, bet_row))
    total = 0
    for i, game in enumerate(sorted(games, key=lambda x: x[0]), start=1):
        total += game[1] * i
    print(total)
    return total
