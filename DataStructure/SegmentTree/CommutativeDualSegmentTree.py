class CommutativeDualSegmentTree:
    def __init__(self, n, unitA, A_f):
        self.n = n
        self.unitA = unitA
        self.A_f = A_f  # (A, A) -> A
        self.A = [unitA] * (n + n)

    def __getitem__(self, i):
        i += self.n
        res = self.unitA
        while i > 0:
            res = self.A_f(res, self.A[i])
            i >>= 1
        return res

    def __setitem__(self, i, val):
        i += self.n
        self.A[i] = val

    def apply(self, i, val):
        i += self.n
        self.A[i] = self.A_f(self.A[i], val)

    def range_apply(self, l, r, val):
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.A[l] = self.A_f(self.A[l], val)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.A_f(self.A[r], val)
            l >>= 1
            r >>= 1
