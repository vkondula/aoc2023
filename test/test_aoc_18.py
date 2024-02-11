import aoc2023


def test_aoc_18_a_base():
    with open("test/inputs/18a_base.txt", "r") as f:
        assert aoc2023.solver18a.solve(f.read()) == 62


def test_aoc_18_a_full():
    with open("test/inputs/18_full.txt", "r") as f:
        assert aoc2023.solver18a.solve(f.read()) == 36679


def test_aoc_18_b_base():
    with open("test/inputs/18b_base.txt", "r") as f:
        assert aoc2023.solver18b.solve(f.read()) == 952408144115


def test_aoc_18_b_full():
    with open("test/inputs/18_full.txt", "r") as f:
        assert aoc2023.solver18b.solve(f.read()) == 88007104020978
