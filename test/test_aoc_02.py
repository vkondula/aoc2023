import aoc2023


def test_aoc_2_a_base():
    with open("test/inputs/02a_base.txt", "r") as f:
        assert aoc2023.solver02a.solve(f.read()) == 8


def test_aoc_2_a_full():
    with open("test/inputs/02_full.txt", "r") as f:
        assert aoc2023.solver02a.solve(f.read()) == 2776


def test_aoc_2_b_base():
    with open("test/inputs/02b_base.txt", "r") as f:
        assert aoc2023.solver02b.solve(f.read()) == 2286


def test_aoc_2_b_full():
    with open("test/inputs/02_full.txt", "r") as f:
        assert aoc2023.solver02b.solve(f.read()) == 68638
