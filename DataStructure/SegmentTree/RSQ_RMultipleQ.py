from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


MOD = 998244353


class RSQ_RMultipleQ(LazySegmentTree):
    def __init__(self, n):
        unitX = 0
        unitA = 1
        X_f = lambda x1, x2: (x1 + x2) % MOD
        A_f = lambda a1, a2: a1 * a2 % MOD
        XA_map = lambda x, a: x * a % MOD
        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)