import aoc2023


def test_aoc_15_a_base():
    with open("test/inputs/15a_base.txt", "r") as f:
        assert aoc2023.solver15a.solve(f.read()) == 1320


def test_aoc_15_a_full():
    with open("test/inputs/15_full.txt", "r") as f:
        assert aoc2023.solver15a.solve(f.read()) == 514281


def test_aoc_15_b_base():
    with open("test/inputs/15b_base.txt", "r") as f:
        assert aoc2023.solver15b.solve(f.read()) == 145


def test_aoc_15_b_full():
    with open("test/inputs/15_full.txt", "r") as f:
        assert aoc2023.solver15b.solve(f.read()) == 244199
