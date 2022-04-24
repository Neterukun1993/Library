from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


class RSQ_RUQ:
    def __init__(self, n):
        unitX = (0, 0)  # (value, size)
        unitA = None
        X_f = lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])
        A_f = lambda a1, a2: a1 if a2 == unitA else a2
        XA_map = lambda x, a: x if a == unitA else (x[1] * a, x[1])
        self.st = LazySegmentTree(n, unitX, unitA, X_f, A_f, XA_map)
        self.st.build([(0, 1) for i in range(n)])

    def build(self, array):
        self.st.build([(x, 1) for x in array])

    def __getitem__(self, i):
        return self.st[i][0]

    def __setitem__(self, i, x):
        self.st[i] = (x, 1)

    def fold(self, l, r):
        return self.st.fold(l, r)[0]

    def apply(self, i, a):
        self.st.apply(i, a)

    def range_apply(self, l, r, a):
        self.st.range_apply(l, r, a)
