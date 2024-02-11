from typing import Optional


class Brick:
    def __init__(self, id: int, coords_one: tuple[int, int, int], coords_two: tuple[int, int, int]):
        self.id = id
        self.coords_one = coords_one
        self.coords_two = coords_two
        self.parts: set[tuple[int, int, int]] = {
            (x, y, z)
            for x in range(coords_one[0], coords_two[0] + 1)
            for y in range(coords_one[1], coords_two[1] + 1)
            for z in range(coords_one[2], coords_two[2] + 1)
        }

    def __repr__(self):
        return f"Brick({self.parts})"

    def moved_down(self) -> Optional[set[tuple[int, int, int]]]:
        new_parts = set(
            (x, y, z - 1)
            for x, y, z in self.parts
        )
        if any(z < 0 for _, _, z in new_parts):
            return None
        return new_parts

    def move_down(self, bricks: dict[int, "Brick"]) -> bool:
        new_parts = self.moved_down()
        if not new_parts:
            return False
        for brick_id, brick in bricks.items():
            if brick_id == self.id:
                continue
            if new_parts & brick.parts:
                return False
        self.parts = new_parts
        return True

    def is_supported_by(self, bricks: dict[int, "Brick"]) -> set[int]:
        moved_down = self.moved_down()
        if not moved_down:
            return set()
        return {
            brick_id
            for brick_id, brick in bricks.items()
            if brick_id != self.id and moved_down & brick.parts
        }


def solve(data_in: str):
    bricks = {}
    for i, line in enumerate(data_in.splitlines()):
        l, r = line.split("~")
        bricks[i] = Brick(i, tuple(int(x) for x in l.split(",")), tuple(int(x) for x in r.split(",")))
    something_changed = True
    while something_changed:
        something_changed = False
        for brick in bricks.values():
            if brick.move_down(bricks):
                something_changed = True
    total = 0
    supports = {i: set() for i in bricks}
    supported_by = {}
    for brick in bricks.values():
        supported_by[brick.id] = brick.is_supported_by(bricks)
        for supported_by_id in supported_by[brick.id]:
            supports[supported_by_id].add(brick.id)
    for brick_id, supporting in supports.items():
        if not supporting:
            total += 1
            continue
        for supporting_id in supporting:
            if len(supported_by[supporting_id]) == 1:
                break
        else:
            total += 1
    print(total)
    return total
