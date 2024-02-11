import aoc2023


def test_aoc_21_a_base():
    with open("test/inputs/21a_base.txt", "r") as f:
        assert aoc2023.solver21a.solve(f.read()) == 16


def test_aoc_21_a_full():
    with open("test/inputs/21_full.txt", "r") as f:
        assert aoc2023.solver21a.solve(f.read()) == 3532


def test_aoc_21_b_base():
    with open("test/inputs/21b_base.txt", "r") as f:
        assert aoc2023.solver21b.solve(f.read()) == 16733044


def test_aoc_21_b_full():
    with open("test/inputs/21_full.txt", "r") as f:
        assert aoc2023.solver21b.solve(f.read()) == 590104708070703
