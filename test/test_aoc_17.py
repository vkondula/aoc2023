import aoc2023


def test_aoc_17_a_base():
    with open("test/inputs/17a_base.txt", "r") as f:
        assert aoc2023.solver17a.solve(f.read()) == 102


def test_aoc_17_a_full():
    with open("test/inputs/17_full.txt", "r") as f:
        assert aoc2023.solver17a.solve(f.read()) == 1260


def test_aoc_17_b_base():
    with open("test/inputs/17b_base.txt", "r") as f:
        assert aoc2023.solver17b.solve(f.read()) == 94


def test_aoc_17_b_full():
    with open("test/inputs/17_full.txt", "r") as f:
        assert aoc2023.solver17b.solve(f.read()) == 1416
