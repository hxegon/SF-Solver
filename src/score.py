from functools import reduce

class Score:

    def __init__(self, init_score):
        self.total = None
        self.string = []
        self.add(init_score)

    def _combine(total, new):
        if total is None or total == 0: # if first in the sequence
            return new
        elif new % 2 == 0: # if even
            return total + new
        elif new % 2 == 1: # if odd
            return total * new

    def _calculate_from(nums):
        return reduce(Score._combine, nums)

    def add(self, new):
        self.total = Score._combine(self.total, new)
        self.string.append(new)

    def add_from(self, news):
        for new in news:
            self.add(new)
