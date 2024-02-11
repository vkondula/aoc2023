import aoc2023


def test_aoc_20_a_base():
    with open("test/inputs/20a_base.txt", "r") as f:
        assert aoc2023.solver20a.solve(f.read()) == 32000000


def test_aoc_20_a_full():
    with open("test/inputs/20_full.txt", "r") as f:
        assert aoc2023.solver20a.solve(f.read()) == 0


def test_aoc_20_b_base():
    with open("test/inputs/20b_base.txt", "r") as f:
        assert aoc2023.solver20b.solve(f.read()) == 818723272


def test_aoc_20_b_full():
    with open("test/inputs/20_full.txt", "r") as f:
        assert aoc2023.solver20b.solve(f.read()) == 243902373381257
