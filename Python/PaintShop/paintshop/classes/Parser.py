import collections


def formatted(line): return line.rstrip('\n').replace(" ", "").replace("\t", "").strip()


def combine_every_n(line, n): return (line[i:i + n] for i in range(0, len(line), n))


class Parser:

    def __init__(self, path):
        self.path = str(path)
        self.input_lines = [formatted(line) for line in open(self.path, "r").read().splitlines() if len(formatted(line)) > 0]
        self.styles_solution = {k: 'G' for k, v in ((color_i+1, 'G') for color_i in range(int(self.input_lines[0])))}
        self.Customer = collections.namedtuple('Customer', ['cust_prefs', 'cust_prefs_count'])
        self.customers = self.gen_customers()

    def gen_customers(self):

        def cust_prefs(line): return dict(((int(string[0]), str(string[1])) for string in combine_every_n(line, 2)))

        return sorted(
            [self.Customer(cust_prefs(line), len(cust_prefs(line))) for line in self.input_lines[1:]]
            , key=lambda cust: cust.cust_prefs_count)
