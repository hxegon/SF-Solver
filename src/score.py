from functools import reduce

class Score:

    def __init__(self, init_score):
        self.total, self.string = None, []
        self.add(init_score)

    def _combine(prev, new):
        if prev is None or prev == 0: # if first in the sequence
            return new
        elif new % 2 == 0: # if even
            return prev + new
        elif new % 2 == 1: # if odd
            return prev * new

    def calculate_from(nums): # for internal use
        return reduce(Score._combine, nums)

    def add(self, new):
        self.total = Score._combine(self.total, new)
        self.string.append(new)

    def add_from(self, news):
        for new in news:
            self.add(new)
