import aoc2023


def test_aoc_9_a_base():
    with open("test/inputs/09a_base.txt", "r") as f:
        assert aoc2023.solver09a.solve(f.read()) == 114


def test_aoc_9_a_full():
    with open("test/inputs/09_full.txt", "r") as f:
        assert aoc2023.solver09a.solve(f.read()) == 1772145754


def test_aoc_9_b_base():
    with open("test/inputs/09b_base.txt", "r") as f:
        assert aoc2023.solver09b.solve(f.read()) == 2


def test_aoc_9_b_full():
    with open("test/inputs/09_full.txt", "r") as f:
        assert aoc2023.solver09b.solve(f.read()) == 867
