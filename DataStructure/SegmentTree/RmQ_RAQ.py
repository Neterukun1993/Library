from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


class RmQ_RAQ(LazySegmentTree):
    def __init__(self, n):
        unitX = (1 << 31) - 1
        unitA = 0
        X_f = min
        A_f = lambda a1, a2: a1 + a2
        XA_map = lambda x, a: x + a
        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)
        super().build([0] * n)
