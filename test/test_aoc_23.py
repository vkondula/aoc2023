import aoc2023


def test_aoc_23_a_base():
    with open("test/inputs/23a_base.txt", "r") as f:
        assert aoc2023.solver23a.solve(f.read()) == 94


def test_aoc_23_a_full():
    with open("test/inputs/23_full.txt", "r") as f:
        assert aoc2023.solver23a.solve(f.read()) == 2010


def test_aoc_23_b_base():
    with open("test/inputs/23b_base.txt", "r") as f:
        assert aoc2023.solver23b.solve(f.read()) == 154


def test_aoc_23_b_full():
    with open("test/inputs/23_full.txt", "r") as f:
        assert aoc2023.solver23b.solve(f.read()) == 6318
