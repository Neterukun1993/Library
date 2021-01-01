class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (self.size + 1)

    def build(self, array):
        for i, val in enumerate(array):
            self.bit[i + 1] = val
        for i in range(1, self.size):
            if i + (i & -i) > self.size:
                continue
            self.bit[i] -= self.bit[i + (i & -i)]

    def __getitem__(self, i):
        i = i + 1
        s = 0
        while i <= self.size:
            s += self.bit[i]
            i += i & -i
        return s

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def add(self, l, r, val):
        """add value in range [l, r)"""
        self._add(r, val)
        self._add(l, -val)
