import aoc2023


def test_aoc_5_a_base():
    with open("test/inputs/05a_base.txt", "r") as f:
        assert aoc2023.solver05a.solve(f.read()) == 35


def test_aoc_5_a_full():
    with open("test/inputs/05_full.txt", "r") as f:
        assert aoc2023.solver05a.solve(f.read()) == 282277027


def test_aoc_5_b_base():
    with open("test/inputs/05b_base.txt", "r") as f:
        assert aoc2023.solver05b.solve(f.read()) == 46


def test_aoc_5_b_full():
    with open("test/inputs/05_full.txt", "r") as f:
        assert aoc2023.solver05b.solve(f.read()) == 11554135
