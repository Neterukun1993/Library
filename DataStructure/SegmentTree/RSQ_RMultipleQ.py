from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


MOD = 998244353


class RSQ_RMultipleQ:
    def __init__(self, n):
        unitX = 0
        unitA = 1
        X_f = lambda x1, x2: (x1 + x2) % MOD
        A_f = lambda a1, a2: a1 * a2 % MOD
        XA_map = lambda x, a: x * a % MOD
        self.st = LazySegmentTree(n, unitX, unitA, X_f, A_f, XA_map)

    def build(self, array):
        self.st.build(array)

    def __getitem__(self, i):
        return self.st[i]

    def __setitem__(self, i, x):
        self.st[i] = x

    def fold(self, l, r):
        return self.st.fold(l, r)

    def apply(self, i, a):
        self.st.apply(i, a)

    def range_apply(self, l, r, a):
        self.st.range_apply(l, r, a)
