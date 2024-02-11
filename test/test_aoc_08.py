import aoc2023


def test_aoc_8_a_base():
    with open("test/inputs/08a_base.txt", "r") as f:
        assert aoc2023.solver08a.solve(f.read()) == 6


def test_aoc_8_a_full():
    with open("test/inputs/08_full.txt", "r") as f:
        assert aoc2023.solver08a.solve(f.read()) == 19783


def test_aoc_8_b_base():
    with open("test/inputs/08b_base.txt", "r") as f:
        assert aoc2023.solver08b.solve(f.read()) == 6


def test_aoc_8_b_full():
    with open("test/inputs/08_full.txt", "r") as f:
        assert aoc2023.solver08b.solve(f.read()) == 9177460370549
