import aoc2023


def test_aoc_11_a_base():
    with open("test/inputs/11a_base.txt", "r") as f:
        assert aoc2023.solver11a.solve(f.read()) == 374


def test_aoc_11_a_full():
    with open("test/inputs/11_full.txt", "r") as f:
        assert aoc2023.solver11a.solve(f.read()) == 10885634


def test_aoc_11_b_base():
    with open("test/inputs/11b_base.txt", "r") as f:
        assert aoc2023.solver11b.solve(f.read()) == 82000210


def test_aoc_11_b_full():
    with open("test/inputs/11_full.txt", "r") as f:
        assert aoc2023.solver11b.solve(f.read()) == 707505470642
