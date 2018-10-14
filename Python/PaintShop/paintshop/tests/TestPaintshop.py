import pathlib

from paintshop.classes.Parser import Parser
from paintshop.classes.Solver import Solver

current_dir = pathlib.Path(__file__).parent

input_paths = [
    "input_0.txt",
    "input_1.txt",
    "input_2.txt",
    "input_3.txt",
    "input_messy_formatting.txt"]

expected_paths = [
    "expected_0.txt",
    "expected_1.txt",
    "expected_2.txt",
    "expected_3.txt",
    "expected_messy_formatting.txt"]


def test_0():
    _test(0)


def test_1():
    _test(1)


def test_2():
    _test(2)


def test_3():
    _test(3)


def test_4():
    _test(4)


def _test(n):
    input_path = pathlib.Path(current_dir / input_paths[n])
    expected_path = pathlib.Path(current_dir / expected_paths[n])

    solution = Solver(Parser(input_path)).solve()
    expected = Solver.to_string([line for line in open(str(expected_path), "r").read().splitlines()])

    assert solution == expected, "Test failed"
    print("Solution:", solution, "Expected:", expected)
