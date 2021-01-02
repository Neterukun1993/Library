from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


class RSQ_RUQ(LazySegmentTree):
    def __init__(self, n):
        unitX = (0, 0)  # (val, size)
        unitA = 10 ** 5
        X_f = lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])
        A_f = lambda a1, a2: a1 if a2 == unitA else a2
        XA_map = lambda x, a: x if a == unitA else (x[1] * a, x[1])
        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)
        super().build([(0, 1) for i in range(n)])

    def build(self, array):
        super().build([(x, 1) for x in array])

    def __getitem__(self, i):
        return super().__getitem__(i)[0]

    def __setitem__(self, i, x):
        super().__setitem__(i, (x, 1))

    def fold(self, l, r):
        return super().fold(l, r)[0]
