import aoc2023


def test_aoc_19_a_base():
    with open("test/inputs/19a_base.txt", "r") as f:
        assert aoc2023.solver19a.solve(f.read()) == 19114


def test_aoc_19_a_full():
    with open("test/inputs/19_full.txt", "r") as f:
        assert aoc2023.solver19a.solve(f.read()) == 353046


def test_aoc_19_b_base():
    with open("test/inputs/19b_base.txt", "r") as f:
        assert aoc2023.solver19b.solve(f.read()) == 167409079868000


def test_aoc_19_b_full():
    with open("test/inputs/19_full.txt", "r") as f:
        assert aoc2023.solver19b.solve(f.read()) == 125355665599537
