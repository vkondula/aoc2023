def get_diff_count(line, line2):
    return len([a for a, b in zip(line, line2) if a != b])


def get_mirror_index(rows: list[str]):
    length = len(rows)
    final_index = None
    for i in range(0, length - 1):
        diff_count = 0
        for j in range(0, i + 1):
            current_index = i - j
            mirror_index = i + j + 1
            if current_index not in range(length) or mirror_index not in range(length):
                break
            diff_count += get_diff_count(rows[current_index], rows[mirror_index])
            if diff_count > 1:
                break
        if diff_count == 1:
            final_index = i
    return final_index


def solve(data_in: str):
    total = 0
    for pattern in data_in.split("\n\n"):
        rows = pattern.split("\n")
        horizontal_index = get_mirror_index(rows)
        transposed_rows = ["".join(row[i] for row in rows) for i in range(len(rows[0]))]
        vertical_index = get_mirror_index(transposed_rows)
        # horizontal = (horizontal_index, 100, len(rows))
        # vertical = (vertical_index, 1, len(transposed_rows[0]))
        # mirror = min(horizontal, vertical, key=lambda x: abs(x[0] - 1 - x[2] / 2))
        if horizontal_index is not None:
            total += (horizontal_index + 1) * 100
        elif vertical_index is not None:
            total += vertical_index + 1
        else:
            raise Exception("No mirror found")
    print(total)
    return total
