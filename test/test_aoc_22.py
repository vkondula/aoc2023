import aoc2023


def test_aoc_22_a_base():
    with open("test/inputs/22a_base.txt", "r") as f:
        assert aoc2023.solver22a.solve(f.read()) == 5


def test_aoc_22_a_full():
    with open("test/inputs/22_full.txt", "r") as f:
        assert aoc2023.solver22a.solve(f.read()) == 413


def test_aoc_22_b_base():
    with open("test/inputs/22b_base.txt", "r") as f:
        assert aoc2023.solver22b.solve(f.read()) == 7


def test_aoc_22_b_full():
    with open("test/inputs/22_full.txt", "r") as f:
        assert aoc2023.solver22b.solve(f.read()) == 41610
