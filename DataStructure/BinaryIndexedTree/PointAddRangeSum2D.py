class BinaryIndexedTree:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.bit = [[0] * (self.w + 1) for _ in range(self.h + 1)]

    def add(self, i, j, val):
        hi, wj = i, j
        i = hi + 1
        while i <= self.h:
            j = wj + 1
            while j <= self.w:
                self.bit[i][j] += val
                j += j & -j
            i += i & -i

    def _sum(self, i, j):
        s, hi, wj = 0, i, j
        i = hi
        while i > 0:
            j = wj
            while j > 0:
                s += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def sum(self, hl, hr, wl, wr):
        """sum of values in range [hl, hr) * [wl, wr)"""
        return self._sum(hr, wr) - self._sum(hl, wr) \
               - self._sum(hr, wl) + self._sum(hl, wl)
