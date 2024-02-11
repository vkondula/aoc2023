import aoc2023


def test_aoc_14_a_base():
    with open("test/inputs/14a_base.txt", "r") as f:
        assert aoc2023.solver14a.solve(f.read()) == 136


def test_aoc_14_a_full():
    with open("test/inputs/14_full.txt", "r") as f:
        assert aoc2023.solver14a.solve(f.read()) == 109466


def test_aoc_14_b_base():
    with open("test/inputs/14b_base.txt", "r") as f:
        assert aoc2023.solver14b.solve(f.read()) == 64


def test_aoc_14_b_full():
    with open("test/inputs/14_full.txt", "r") as f:
        assert aoc2023.solver14b.solve(f.read()) == 94585
