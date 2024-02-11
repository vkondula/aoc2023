from typing import Optional


def add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]


def in_range_2d(v, boundary):
    return boundary[0] <= v[0] <= boundary[1] and boundary[0] <= v[1] <= boundary[1]


def in_future(p1, p2, q):
    if p1[0] < p2[0]:
        return q[0] >= p1[0]
    return q[0] <= p1[0]


def intersection_of_lines_2d(
        p1: tuple[int, int, int],
        p2: tuple[int, int, int],
        q1: tuple[int, int, int],
        q2: tuple[int, int, int]
) -> Optional[tuple[float, float]]:
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = q1
    x4, y4, _ = q2
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    intersection_x = x1 + t * (x2 - x1)
    intersection_y = y1 + t * (y2 - y1)
    return intersection_x, intersection_y


def solve(data_in: str):
    boundary = (7, 27) if len(data_in.splitlines()) < 10 else (200000000000000, 400000000000000)
    hailstorms = []
    for line in data_in.splitlines():
        p_raw, v_raw = line.split("@")
        p = tuple(int(x.strip(" ")) for x in p_raw.split(","))
        v = tuple(int(x.strip(" ")) for x in v_raw.split(","))
        q = add(p, v)
        hailstorms.append((p, q))
    total = 0
    for i in range(len(hailstorms)):
        for j in range(i + 1, len(hailstorms)):
            if p := intersection_of_lines_2d(*hailstorms[i], *hailstorms[j]):
                if in_range_2d(p, boundary) and in_future(*hailstorms[i], p) and in_future(*hailstorms[j], p):
                    total += 1
    print(total)
    return total