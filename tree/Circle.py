import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


class Circle:
    def __init__(self, data, nrtimes):
        self.data = data
        self.nrtimes = nrtimes

    def __iter__(self):
        total_len = int(round_up(self.nrtimes / len(self.data)))
        for i in range(total_len):
            for item in self.data:
                yield item

    def __str__(self):
        return f'Circle({self.data}, {self.nrtimes})'


c = Circle('abc', 9)
print(list(c))
