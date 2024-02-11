import re

def hash_(label: str):
    total = 0
    for char in label:
        total += ord(char)
        total *= 17
        total %= 256
    return total


def solve(data_in: str):
    boxes = [{} for _ in range(256)]
    for item in data_in.split(","):
        name = re.search(r"[a-z]+", item)[0]
        box_index = hash_(name)
        if "-" in item and name in boxes[box_index]:
            boxes[box_index].pop(name)
        if "=" in item:
            value = int(item.split("=")[1])
            boxes[box_index][name] = value
    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, value in enumerate(box.values(), start=1):
            total += j * i * value
    print(total)
    return total

