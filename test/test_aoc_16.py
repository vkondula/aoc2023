import aoc2023


def test_aoc_16_a_base():
    with open("test/inputs/16a_base.txt", "r") as f:
        assert aoc2023.solver16a.solve(f.read()) == 46


def test_aoc_16_a_full():
    with open("test/inputs/16_full.txt", "r") as f:
        assert aoc2023.solver16a.solve(f.read()) == 7482


def test_aoc_16_b_base():
    with open("test/inputs/16b_base.txt", "r") as f:
        assert aoc2023.solver16b.solve(f.read()) == 51


def test_aoc_16_b_full():
    with open("test/inputs/16_full.txt", "r") as f:
        assert aoc2023.solver16b.solve(f.read()) == 7896
