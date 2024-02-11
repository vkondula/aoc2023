import aoc2023


def test_aoc_10_a_base():
    with open("test/inputs/10a_base.txt", "r") as f:
        assert aoc2023.solver10a.solve(f.read()) == 8


def test_aoc_10_a_full():
    with open("test/inputs/10_full.txt", "r") as f:
        assert aoc2023.solver10a.solve(f.read()) == 6717


def test_aoc_10_b_base():
    with open("test/inputs/10b_base.txt", "r") as f:
        assert aoc2023.solver10b.solve(f.read()) == 10


def test_aoc_10_b_full():
    with open("test/inputs/10_full.txt", "r") as f:
        assert aoc2023.solver10b.solve(f.read()) == 381
