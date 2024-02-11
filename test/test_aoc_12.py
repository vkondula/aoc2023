import aoc2023


def test_aoc_12_a_base():
    with open("test/inputs/12a_base.txt", "r") as f:
        assert aoc2023.solver12a.solve(f.read()) == 21


def test_aoc_12_a_full():
    with open("test/inputs/12_full.txt", "r") as f:
        assert aoc2023.solver12a.solve(f.read()) == 7204


def test_aoc_12_b_base():
    with open("test/inputs/12b_base.txt", "r") as f:
        assert aoc2023.solver12b.solve(f.read()) == 525152


def test_aoc_12_b_full():
    with open("test/inputs/12_full.txt", "r") as f:
        assert aoc2023.solver12b.solve(f.read()) == 1672318386674
