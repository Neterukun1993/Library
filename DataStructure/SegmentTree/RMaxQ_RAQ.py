from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


class RMaxQ_RAQ:
    def __init__(self, n):
        unitX = -((1 << 31) - 1)
        unitA = 0
        X_f = max
        A_f = lambda a1, a2: a1 + a2
        XA_map = lambda x, a: x + a
        self.st = LazySegmentTree(n, unitX, unitA, X_f, A_f, XA_map)
        self.st.build([0] * n)

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
