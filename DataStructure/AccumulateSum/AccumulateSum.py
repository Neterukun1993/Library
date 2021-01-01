class AccumulateSum:
    def __init__(self, array):
        self.n = len(array)
        self.cumsum = [0] * (self.n + 1)
        for i, val in enumerate(array):
            self.cumsum[i + 1] = self.cumsum[i] + val

    def sum(self, l, r):
        return self.cumsum[r] - self.cumsum[l]
