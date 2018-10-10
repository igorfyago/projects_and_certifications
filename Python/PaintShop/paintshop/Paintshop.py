from paintshop.classes.Solver import *


def main():
    path = "D:/GitHub/projects_and_certifications/Python/PaintShop/paintshop/tests/input.txt"
    solution = Solver(path).solve()
    print(solution)


if __name__ == '__main__':
    main()

"""
#path1 = sys.argv[1]
#input_obj = FormatInput(str(path1))
#solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
#solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
##print(solution)
"""
