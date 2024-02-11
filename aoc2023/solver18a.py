def solve(data_in: str):
    total = 0
    width = 0
    commands = []
    for row in data_in.splitlines():
        command, length_raw, _ = row.split(" ")
        length = int(length_raw)
        commands.append((command, length))
    for i, (command, length) in enumerate(commands):
        next_command = commands[(i + 1) % len(commands)][0]
        previous_command = commands[(i - 1) % len(commands)][0]
        if command == "R":
            next_diff = {"D": 1, "U": 0}
            previous_diff = {"D": -1, "U": 0}
            width += length + next_diff[next_command] + previous_diff[previous_command]
        elif command == "L":
            next_diff = {"D": 0, "U": 1}
            previous_diff = {"D": 0, "U": -1}
            width -= length + next_diff[next_command] + previous_diff[previous_command]
        elif command == "D":
            next_diff = {"R": 0, "L": 1}
            previous_diff = {"R": 0, "L": -1}
            total += (length + next_diff[next_command] + previous_diff[previous_command]) * width
        elif command == "U":
            next_diff = {"R": 1, "L": 0}
            previous_diff = {"R": -1, "L": 0}
            total -= (length + next_diff[next_command] + previous_diff[previous_command]) * width
    print(total)
    return total
