import re
from collections import defaultdict

MAX_CUBES = {"green": 13, "red": 12, "blue": 14}


def solve(data_in: str):
    # format: `Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red`
    sum_game_ids = 0
    for row in data_in.split("\n"):
        game, rounds_raw = row.split(":")
        game_id = int(game.split(" ")[1])
        try:
           for round_raw in rounds_raw.split(";"):
               used = defaultdict(int)
               for colour in ["green", "red", "blue"]:
                   if match := re.search(r"(\d+) {}".format(colour), round_raw):
                        used[colour] = int(match.group(1))
               for key, value in used.items():
                   if value > MAX_CUBES[key]:
                       raise ValueError()
        except ValueError:
           pass
        else:
           sum_game_ids += game_id
    print(sum_game_ids)
    return sum_game_ids
