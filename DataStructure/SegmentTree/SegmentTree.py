class SegmentTree:
    def __init__(self, n, op, e):
        self.n = n
        self.op = op
        self.e = e
        self.size = 2 ** ((n - 1).bit_length())
        self.node = [self.e] * (2 * self.size)

    def __getitem__(self, i):
        return self.node[i + self.size]

    def __setitem__(self, i, val):
        i += self.size
        self.node[i] = val
        while i > 1:
            i >>= 1
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def build(self, array):
        for i, val in enumerate(array, self.size):
            self.node[i] = val
        for i in range(self.size - 1, 0, -1):
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def all_fold(self):
        return self.node[1]

    def fold(self, l, r):
        l, r = l + self.size, r + self.size
        vl, vr = self.e, self.e
        while l < r:
            if l & 1:
                vl = self.op(vl, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.op(self.node[r], vr)
            l, r = l >> 1, r >> 1
        return self.op(vl, vr)

    def max_right(self, l, f):
        if l == self.n:
            return self.n
        l += self.size
        v = self.e
        init = True
        while init or (l & -l) != l:
            init = False
            while l % 2 == 0:
                l >>= 1
            if not f(self.op(v, self.node[l])):
                while l < self.size:
                    l <<= 1
                    if f(self.op(v, self.node[l])):
                        v = self.op(v, self.node[l])
                        l += 1
                return l - self.size
            v = self.op(v, self.node[l])
            l += 1
        return self.n
