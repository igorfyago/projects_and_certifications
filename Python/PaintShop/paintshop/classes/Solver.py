from paintshop.classes.Parser import *
from paintshop.classes.Customer import *


def list_to_string(arg):
    if type(arg) is list:
        arg = " ".join(arg)
    return arg


class Solver:

    def __init__(self, path):
        self.shop_styles = Parser(str(path)).shop_styles

    def solve(self):

        def cust_validate(shop_styles, cust):
            for color, pref_style in cust.cust_prefs.items():
                if shop_styles[color - 1] == pref_style:
                    cust.cust_satisfied = True
                    return True, None, None
            return False, color, pref_style

        def run():
            for stage in iter(['solve', 'validate']):
                for cust in Customer:
                    cust_satisfied, update_color, update_style = cust_validate(self.shop_styles, cust)
                    if not cust_satisfied:
                        if stage == 'solve' and update_style == 'M':
                            self.shop_styles[update_color-1] = 'M'
                        else:
                            return "No solution exists"
            return list_to_string(self.shop_styles)

        return run()
