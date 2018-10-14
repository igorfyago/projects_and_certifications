import pathlib
import sys

from paintshop.classes.Parser import Parser
from paintshop.classes.Solver import Solver

input_paths = [
    'input_0.txt',
    'input_1.txt',
    'input_2.txt',
    'input_3.txt',
    'input_messy_formatting.txt']


def main():
    path = pathlib.Path(pathlib.Path(__file__).parent / 'tests' / input_paths[2])
    # path = sys.argv[1]
    solution = Solver(Parser(path)).solve()
    print(solution)


if __name__ == '__main__':
    main()