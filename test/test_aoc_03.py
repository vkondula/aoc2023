import aoc2023


def test_aoc_3_a_base():
    with open("test/inputs/03a_base.txt", "r") as f:
        assert aoc2023.solver03a.solve(f.read()) == 4361


def test_aoc_3_a_full():
    with open("test/inputs/03_full.txt", "r") as f:
        assert aoc2023.solver03a.solve(f.read()) == 554003


def test_aoc_3_b_base():
    with open("test/inputs/03b_base.txt", "r") as f:
        assert aoc2023.solver03b.solve(f.read()) == 467835


def test_aoc_3_b_full():
    with open("test/inputs/03_full.txt", "r") as f:
        assert aoc2023.solver03b.solve(f.read()) == 87263515
