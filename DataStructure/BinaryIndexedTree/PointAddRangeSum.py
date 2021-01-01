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
            self.bit[i + (i & -i)] += self.bit[i]

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, val):
        i += 1
        while i <= self.size:
            self.bit[i] += val
            i += i & -i

    def sum(self, l, r):
        """sum of values in range [l, r)"""
        return self._sum(r) - self._sum(l)

    def bisect_left(self, val):
        """minimum idx s.t. sum[0, idx) >= val"""
        if val <= 0:
            return 0
        idx = 0
        k = 1 << self.size.bit_length()
        while k:
            if idx + k <= self.size and self.bit[idx + k] < val:
                val -= self.bit[idx + k]
                idx += k
            k >>= 1
        return idx + 1
