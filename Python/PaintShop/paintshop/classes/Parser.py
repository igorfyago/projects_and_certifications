from paintshop.classes.Customer import *


def combine_every(line, n): return [line[i:i + n] for i in range(0, len(line), n)]


def valid(line): return line.rstrip('\n').replace(" ", "").replace("\t", "").strip()


class Parser:
    def __init__(self, path):
        self.input_lines = [valid(line) for line in open(path, "r").read().splitlines() if len(valid(line)) > 0]
        self.shop_styles = ['G' for style in range(int(self.input_lines[0]))]
        self.add_customers()

    def add_customers(self):
        for row_id, line in enumerate(self.input_lines[1:]):
            cust_prefs = dict([[int(string[0]), str(string[1])] for string in combine_every(line,2)])
            Customer("cust_" + str(row_id + 1), cust_prefs, len(cust_prefs))
