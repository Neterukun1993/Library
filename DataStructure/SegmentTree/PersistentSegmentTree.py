class PSTNode:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


class PersistentSegmentTree:
    def __init__(self, op, e, root=None):
        self.op = op
        self.e = e
        self.root = root

    def build(self, array):
        n = len(array)
        self.log = (n - 1).bit_length()
        self.size = 2 ** self.log
        array = [PSTNode(array[i] if i < n else self.e) for i in range(self.size)]
        tmp = []
        for h in range(self.log):
            for i in range(1 << (self.log - h - 1)):
                nd = self.make_parent(array[i << 1 | 0], array[i << 1 | 1])
                tmp.append(nd)
            array, tmp = tmp, array
        self.root = array[0]

    def __getitem__(self, i):
        nd = self.root
        for h in range(self.log):
            if (i >> (self.log - h - 1)) & 1:
                nd = nd.r
            else:
                nd = nd.l
        return nd.val

    def update(self, i, val):
        nd = self.root
        stack = []
        for h in range(self.log):
            stack.append(nd)
            if (i >> (self.log - h - 1)) & 1:
                nd = nd.r
            else:
                nd = nd.l
        nd = PSTNode(val)
        for ndp in reversed(stack):
            if ndp.l is nd:
                nd = make_parent(nd, nd.r)
            else:
                nd = make_parent(nd.l, nd)
        return PersistentSegmentTree(self.op, self.e, nd)

    def make_parent(self, ndl, ndr):
        val = self.op(ndl.val, ndr.val)
        nd = PSTNode(val)
        nd.l, nd.r = ndl, ndr
        return nd

    def all_fold(self):
        return self.root.val

    def fold(self, l, r):
        return self._fold(l, r, 0, self.n, self.root)

    def _fold(self, a, b, k, l, r, nd):
        if r <= a or b <= l:
            return self.e
        if a <= l and r <= b:
            return self.nd.val
        vl = self._fold(a, b, l, (l + r) >> 1, nd.l)
        vr = self._fold(a, b, (l + r) >> 1, r, nd.r)
        return self.op(vl, vr)
