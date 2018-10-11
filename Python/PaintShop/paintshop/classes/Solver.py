class Solver:

    def __init__(self, parser, customers):
        self.parser = parser
        self.customers = customers

    def solve(self):

        def cust_validate(cust):
            for color, pref_style in cust.cust_prefs.items():
                if cust.styles_solution[color - 1] == pref_style:
                    cust.cust_satisfied = True
                    return True, None, None
            return False, color, pref_style

        def run():
            for stage in iter(['solve', 'validate']):
                for cust in self.customers:
                    cust_satisfied, update_color, update_style = cust_validate(cust)
                    if not cust_satisfied:
                        if stage == 'solve' and update_style == 'M':
                            cust.styles_solution[update_color-1] = 'M'
                        else:
                            return "No solution exists"
            return self.list_to_string(self.customers.styles_solution)

        return run()

    @staticmethod
    def list_to_string(arg):
        if type(arg) is list:
            arg = " ".join(arg)
        return arg
