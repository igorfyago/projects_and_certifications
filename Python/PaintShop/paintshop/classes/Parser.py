def combine_every(line, n): return [line[i:i + n] for i in range(0, len(line), n)]


def formatted(line): return line.rstrip('\n').replace(" ", "").replace("\t", "").strip()


class Parser:
    path = ""

    def __init__(self, path):
        Parser.path = str(path)
        self.input_lines = [formatted(line) for line in open(self.path, "r").read().splitlines() if len(formatted(line)) > 0]
        self.amount_requested_colors = int(self.input_lines[0])
        self.styles_solution = ['G' for style in range(self.amount_requested_colors)]

        self.set_amount_requested_colors()
        self.set_styles_solution()
        self.add_customers()

    def add_customers(self):
        for row_id, line in enumerate(self.input_lines[1:]):
            cust_prefs = dict([[int(string[0]), str(string[1])] for string in combine_every(line,2)])
            Customer("cust_" + str(row_id + 1), cust_prefs, len(cust_prefs), self.path)

    def set_amount_requested_colors(self):
        Customer.amount_requested_colors = self.amount_requested_colors

    def set_styles_solution(self):
        Customer.styles_solution = self.styles_solution


class SortedCustomer(type):
    def __iter__(cls):
        all_cust = cls._all_cust
        all_cust = [cust for cust in all_cust if cust.path == Parser.path]
        all_cust.sort(key=lambda cust: cust.cust_prefs_count, reverse=False)
        return iter(all_cust)


class Customer(Parser, metaclass=SortedCustomer):
    _all_cust= []
    amount_ordered_colors = 0
    styles_solution = []

    def __init__(self, cust_id, cust_prefs, cust_prefs_count, path):
        self._all_cust.append(self)
        self.cust_id = cust_id
        self.cust_prefs = cust_prefs
        self.cust_prefs_count = cust_prefs_count
        self.path = path

    def print_cust_vars(self):
        print(self.cust_id, self.cust_prefs, self.cust_prefs_count, self.path)

    @staticmethod
    def print_all():
        for cust in Customer:
            cust.print_cust_vars()
