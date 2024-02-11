import aoc2023


def test_aoc_1_a_base():
    with open("test/inputs/01a_base.txt", "r") as f:
        assert aoc2023.solver01a.solve(f.read()) == 142


def test_aoc_1_a_full():
    with open("test/inputs/01_full.txt", "r") as f:
        assert aoc2023.solver01a.solve(f.read()) == 54601


def test_aoc_1_b_base():
    with open("test/inputs/01b_base.txt", "r") as f:
        assert aoc2023.solver01b.solve(f.read()) == 281


def test_aoc_1_b_full():
    with open("test/inputs/01_full.txt", "r") as f:
        assert aoc2023.solver01b.solve(f.read()) == 54078
