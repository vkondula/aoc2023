import aoc2023


def test_aoc_13_a_base():
    with open("test/inputs/13a_base.txt", "r") as f:
        assert aoc2023.solver13a.solve(f.read()) == 405


def test_aoc_13_a_full():
    with open("test/inputs/13_full.txt", "r") as f:
        assert aoc2023.solver13a.solve(f.read()) == 34772


def test_aoc_13_b_base():
    with open("test/inputs/13b_base.txt", "r") as f:
        assert aoc2023.solver13b.solve(f.read()) == 400


def test_aoc_13_b_full():
    with open("test/inputs/13_full.txt", "r") as f:
        assert aoc2023.solver13b.solve(f.read()) == 35554
