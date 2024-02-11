import aoc2023


def test_aoc_6_a_base():
    with open("test/inputs/06a_base.txt", "r") as f:
        assert aoc2023.solver06a.solve(f.read()) == 288


def test_aoc_6_a_full():
    with open("test/inputs/06_full.txt", "r") as f:
        assert aoc2023.solver06a.solve(f.read()) == 0


def test_aoc_6_b_base():
    with open("test/inputs/06b_base.txt", "r") as f:
        assert aoc2023.solver06b.solve(f.read()) == 71503


def test_aoc_6_b_full():
    with open("test/inputs/06_full.txt", "r") as f:
        assert aoc2023.solver06b.solve(f.read()) == 39570185
