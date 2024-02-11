import aoc2023


def test_aoc_7_a_base():
    with open("test/inputs/07a_base.txt", "r") as f:
        assert aoc2023.solver07a.solve(f.read()) == 6440


def test_aoc_7_a_full():
    with open("test/inputs/07_full.txt", "r") as f:
        assert aoc2023.solver07a.solve(f.read()) == 250062426


def test_aoc_7_b_base():
    with open("test/inputs/07b_base.txt", "r") as f:
        assert aoc2023.solver07b.solve(f.read()) == 5905


def test_aoc_7_b_full():
    with open("test/inputs/07_full.txt", "r") as f:
        assert aoc2023.solver07b.solve(f.read()) == 250506580
