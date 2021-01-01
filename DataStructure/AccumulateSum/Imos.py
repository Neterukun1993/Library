class Imos:
    def __init__(self, n):
        self.n = n
        self.imos = [0] * (self.n + 1)

    def __getitem__(self, i):
        return self.imos[i]

    def add(self, l, r, val):
        """add value in range [l, r)"""
        self.imos[r] -= val
        self.imos[l] += val

    def build(self):
        for i in range(self.n):
            self.imos[i + 1] += self.imos[i]
