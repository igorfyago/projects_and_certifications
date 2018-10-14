from collections import namedtuple


def formatted(line): return line.rstrip('\n').replace(' ', '').replace('\t', '').strip()


def combine_every_n(line, n): return (line[i:i + n] for i in range(0, len(line), n))


def preferences(line): return dict(((int(string[0]), str(string[1])) for string in combine_every_n(line, 2)))


class Parser:

    def __init__(self, path):
        self.path = str(path)

        self.input_lines = [formatted(line) for line in open(self.path, 'r').read().splitlines() if len(formatted(line)) > 0]

        self.styles_solution = {k: 'G' for k, v in ((color_i + 1, 'G') for color_i in range(int(self.input_lines[0])))}

        self.Customers = namedtuple('Customers', ['id', 'preferences', 'preferences_count'])

        self.customers = sorted(
            [self.Customers(row, preferences(line), len(preferences(line))) for row, line in enumerate(self.input_lines[1:])]
            , key=lambda customer: customer.preferences_count)
