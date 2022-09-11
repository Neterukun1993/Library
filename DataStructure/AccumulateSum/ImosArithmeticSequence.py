class ImosArithmeticSequence:
    def __init__(self, n):
        self.n = n
        self.imos0 = [0] * (self.n + 1)
        self.imos1 = [0] * (self.n + 1)

    def __getitem__(self, i):
        return self.imos0[i] + self.imos1[i] * i

    def add(self, l, r, a, d):
        self.imos0[l] += a
        self.imos0[r] -= a
        self.imos0[l] -= d * l
        self.imos0[r] += d * l
        self.imos1[l] += d
        self.imos1[r] -= d

    def build(self):
        for i in range(self.n):
            self.imos0[i + 1] += self.imos0[i]
            self.imos1[i + 1] += self.imos1[i]
