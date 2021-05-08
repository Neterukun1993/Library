class BinaryIndexedTree:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.bit = [[0] * (self.w + 1) for _ in range(self.h + 1)]

    def get(self, i, j):
        j0 = j
        i = i + 1
        s = 0
        while i <= self.h:
            j = j0 + 1
            while j <= self.w:
                s += self.bit[i][j]
                j += j & -j
            i += i & -i
        return s

    def _add(self, i, j, val):
        j0 = j
        while i > 0:
            j = j0
            while j > 0:
                self.bit[i][j] += val
                j -= j & -j
            i -= i & -i

    def add(self, hl, hr, wl, wr, val):
        """add value in range [l, r)"""
        self._add(hl, wl, val)
        self._add(hr, wl, -val)
        self._add(hl, wr, -val)
        self._add(hr, wr, val)
