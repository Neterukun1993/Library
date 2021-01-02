from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


class RmQ_RUQ(LazySegmentTree):
    def __init__(self, n):
        unitX = (1 << 31) - 1
        unitA = -1
        X_f = min
        A_f = lambda a1, a2: a1 if a2 == self.unitA else a2
        XA_map = lambda x, a: x if a == self.unitA else a
        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)
