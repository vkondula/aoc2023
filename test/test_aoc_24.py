import aoc2023


def test_aoc_24_a_base():
    with open("test/inputs/24a_base.txt", "r") as f:
        assert aoc2023.solver24a.solve(f.read()) == 2


def test_aoc_24_a_full():
    with open("test/inputs/24_full.txt", "r") as f:
        assert aoc2023.solver24a.solve(f.read()) == 16727


def test_aoc_24_b_base():
    with open("test/inputs/24b_base.txt", "r") as f:
        assert aoc2023.solver24b.solve(f.read()) == 47


def test_aoc_24_b_full():
    with open("test/inputs/24_full.txt", "r") as f:
        assert aoc2023.solver24b.solve(f.read()) == 606772018765659
