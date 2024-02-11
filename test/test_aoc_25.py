import aoc2023


def test_aoc_25_a_base():
    with open("test/inputs/25a_base.txt", "r") as f:
        assert aoc2023.solver25a.solve(f.read()) == 54


def test_aoc_25_a_full():
    with open("test/inputs/25_full.txt", "r") as f:
        assert aoc2023.solver25a.solve(f.read()) == 589036


def test_aoc_25_b_base():
    with open("test/inputs/25b_base.txt", "r") as f:
        assert aoc2023.solver25b.solve(f.read()) == 0


def test_aoc_25_b_full():
    with open("test/inputs/25_full.txt", "r") as f:
        assert aoc2023.solver25b.solve(f.read()) == 0
