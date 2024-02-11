import aoc2023


def test_aoc_4_a_base():
    with open("test/inputs/04a_base.txt", "r") as f:
        assert aoc2023.solver04a.solve(f.read()) == 13


def test_aoc_4_a_full():
    with open("test/inputs/04_full.txt", "r") as f:
        assert aoc2023.solver04a.solve(f.read()) == 21088


def test_aoc_4_b_base():
    with open("test/inputs/04b_base.txt", "r") as f:
        assert aoc2023.solver04b.solve(f.read()) == 30


def test_aoc_4_b_full():
    with open("test/inputs/04_full.txt", "r") as f:
        assert aoc2023.solver04b.solve(f.read()) == 6874754
