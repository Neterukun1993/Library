from DataStructure.SegmentTree.CommutativeDualSegmentTree import CommutativeDualSegmentTree


class RUQ(CommutativeDualSegmentTree):
    def __init__(self, n):
        unitA = (0, 0)
        A_f = lambda a1, a2: a2 if a2 > a1 else a1
        super().__init__(n, unitA, A_f)
        self.cnt = 1

    def __getitem__(self, i):
        return super().__getitem__(i)[1]

    def __setitem__(self, i, val):
        self.cnt += 1
        super().__setitem__(i, (self.cnt, val))

    def apply(self, i, val):
        self.cnt += 1
        super().apply(i, (self.cnt, val))

    def range_apply(self, l, r, val):
        self.cnt += 1
        super().range_apply(l, r, (self.cnt, val))
