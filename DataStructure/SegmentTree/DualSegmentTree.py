class DualSegmentTree:
    def __init__(self, n, unitA, A_f):
        self.n = n
        self.unitA = unitA
        self.A_f = A_f  # (A, A) -> A
        self.A = [unitA] * (n + n)

    def __getitem__(self, i):
        i += self.n
        self._propagate_above(i)
        return self.A[i]

    def __setitem__(self, i, val):
        i += self.n
        self._propagate_above(i)
        self.A[i] = val

    def _propagate_above(self, i):
        k = i >> 1
        H = k.bit_length() - 1
        for h in range(H, -1, -1):
            i = k >> h
            if self.A[i] == self.unitA:
                continue
            self.A[i << 1 | 0] = self.A_f(self.A[i << 1 | 0], self.A[i])
            self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
            self.A[i] = self.unitA

    def apply(self, i, val):
        i += self.n
        self._propagate_above(i)
        self.A[i] = self.A_f(self.A[i], val)

    def range_apply(self, l, r, val):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self._propagate_above(l0)
        self._propagate_above(r0)
        while l < r:
            if l & 1:
                self.A[l] = self.A_f(self.A[l], val)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.A_f(self.A[r], val)
            l >>= 1
            r >>= 1
