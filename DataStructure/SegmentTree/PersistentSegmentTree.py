class PersistentSegmentTree:
    def __init__(self, n, op, e, root=None):
        self.op = op
        self.e = e
        self.root = root
        self.n = n
        self.log = (n - 1).bit_length()
        self.size = 2 ** self.log

    def build(self, array):
        array = [(None, None, array[i] if i < self.n else self.e) for i in range(self.size)]
        for h in range(self.log):
            tmp = []
            for i in range(1 << (self.log - h - 1)):
                nd = self.make_parent(array[i << 1 | 0], array[i << 1 | 1])
                tmp.append(nd)
            array, tmp = tmp, array
        self.root = array[0]

    def __getitem__(self, i):
        nd = self.root
        for h in range(self.log):
            if (i >> (self.log - h - 1)) & 1:
                nd = nd[1]
            else:
                nd = nd[0]
        return nd[2]

    def update(self, i, val):
        nd = self.root
        stack = [nd]
        for h in range(self.log):
            if (i >> (self.log - h - 1)) & 1:
                nd = nd[1]
            else:
                nd = nd[0]
            stack.append(nd)
        nd = (None, None, val)
        for ndc, ndp in zip(stack[::-1], stack[::-1][1:]):
            if ndp[0] is ndc:
                nd = self.make_parent(nd, ndp[1])
            else:
                nd = self.make_parent(ndp[0], nd)
        return PersistentSegmentTree(self.size, self.op, self.e, nd)

    def make_parent(self, ndl, ndr):
        return (ndl, ndr, self.op(ndl[2], ndr[2]))

    def all_fold(self):
        return self.root[2]

    def fold(self, l, r):
        return self._fold(l, r, 0, self.n, self.root)

    def _fold(self, a, b, l, r, nd):
        if r <= a or b <= l:
            return self.e
        if a <= l and r <= b:
            return nd[2]
        vl = self._fold(a, b, l, (l + r) >> 1, nd[0])
        vr = self._fold(a, b, (l + r) >> 1, r, nd[1])
        return self.op(vl, vr)
