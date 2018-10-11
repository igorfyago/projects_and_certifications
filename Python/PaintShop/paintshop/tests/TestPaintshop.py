import pathlib

from paintshop.classes.Parser import Parser
from paintshop.classes.Parser import Customer
from paintshop.classes.Solver import Solver

current_dir = pathlib.Path(__file__).parent

input_paths = [
    "input_0.txt",
    "input_1.txt",
    "input_2.txt",
    "input_3.txt"]

expected_paths = [
    "expected_0.txt",
    "expected_1.txt",
    "expected_2.txt",
    "expected_3.txt"]


def test_0():
    _test_(0)


def test_1():
    _test_(1)


def test_2():
    _test_(2)


def test_3():
    _test_(3)


def _test_(n):
    input_path = pathlib.Path(current_dir / input_paths[n])
    expected_path = pathlib.Path(current_dir / expected_paths[n])

    solution = Solver(Parser(input_path), Customer).solve()
    expected = Solver.list_to_string([line for line in open(str(expected_path), "r").read().splitlines()])

    assert solution == expected, "Test failed"
    print("Solution:", solution, "Expected:", expected)
