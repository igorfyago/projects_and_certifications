NO_SOLUTION = "No solution exists"


class Solver:

    def __init__(self, parser, customers):
        self.parser = parser
        self.customers = customers

    def solve(self):

        def cust_validate(cust):
            for color, pref_style in cust.cust_prefs.items():
                if self.parser.styles_solution[color] == pref_style:
                    cust.cust_satisfied = True
                    return True, None, None
            return False, color, pref_style

        def run():
            for stage in iter(['solve', 'validate']):
                for cust in self.customers:
                    cust_satisfied, update_color, update_style = cust_validate(cust)
                    if not cust_satisfied:
                        if stage == 'solve' and update_style == 'M':
                            self.parser.styles_solution[update_color] = 'M'
                        else:
                            return NO_SOLUTION
            return self.to_string(self.parser.styles_solution)

        return run()

    @staticmethod
    def to_string(arg):
        if type(arg) is dict:
            arg = " ".join(list(arg.values()))
        elif type(arg) is list:
            arg = " ".join(arg)
        return arg
