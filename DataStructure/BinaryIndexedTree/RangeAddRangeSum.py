class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.bit0 = [0] * (self.size + 1)
        self.bit1 = [0] * (self.size + 1)

    def _add(self, bit, i, val):
        i = i + 1
        while i <= self.size:
            bit[i] += val
            i += i & -i

    def _sum(self, bit, i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def add(self, l, r, val):
        """add value in range [l, r)"""
        self._add(self.bit0, l, -val * l)
        self._add(self.bit0, r, val * r)
        self._add(self.bit1, l, val)
        self._add(self.bit1, r, -val)

    def sum(self, l, r):
        """sum of values in range [l, r)"""
        return self._sum(self.bit0, r) + r * self._sum(self.bit1, r)\
               - self._sum(self.bit0, l) - l * self._sum(self.bit1, l)
