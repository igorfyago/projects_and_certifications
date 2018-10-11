import sys

from paintshop.classes.Parser import Parser
from paintshop.classes.Parser import Customer
from paintshop.classes.Solver import Solver


def main():
    # path = "D:/GitHub/projects_and_certifications/Python/PaintShop/paintshop/tests/input_0.txt"
    path = sys.argv[1]
    solution = Solver(Parser(path), Customer).solve()
    print(solution)


if __name__ == '__main__':
    main()
