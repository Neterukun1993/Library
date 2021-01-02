class LazySegmentTree:
    def __init__(self, n, unitX, unitA, X_f, A_f, XA_map):
        self.n = n
        self.unitX = unitX
        self.unitA = unitA
        self.X_f = X_f  # (X, X) -> X
        self.A_f = A_f  # (A, A) -> A
        self.XA_map = XA_map  # (X, A) -> X
        self.X = [unitX] * (n + n)
        self.A = [unitA] * (n + n)

    def __getitem__(self, i):
        i += self.n
        self._propagate_above(i)
        return self.X[i]

    def __setitem__(self, i, x):
        i += self.n
        self._propagate_above(i)
        self.X[i] = x
        self._calc_above(i)

    def build(self, array):
        for i, val in enumerate(array, self.n):
            self.X[i] = val
        for i in range(self.n - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _calc_above(self, i):
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _propagate_above(self, i):
        k = i >> 1
        H = k.bit_length() - 1
        for h in range(H, -1, -1):
            i = k >> h
            if self.A[i] == self.unitA:
                continue
            self.X[i << 1] = self.XA_map(self.X[i << 1], self.A[i])
            self.X[i << 1 | 1] = self.XA_map(self.X[i << 1 | 1], self.A[i])
            self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])
            self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
            self.A[i] = self.unitA

    def fold(self, l, r):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self._propagate_above(l0)
        self._propagate_above(r0)
        xl = self.unitX
        xr = self.unitX
        while l < r:
            if l & 1:
                xl = self.X_f(xl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                xr = self.X_f(self.X[r], xr)
            l >>= 1
            r >>= 1
        return self.X_f(xl, xr)

    def apply(self, i, a):
        i += self.n
        self._propagate_above(i)
        self.X[i] = self.XA_map(self.X[i], a)
        self.A[i] = self.A_f(self.A[i], a)
        self._calc_above(i)

    def range_apply(self, l, r, a):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self._propagate_above(l0)
        self._propagate_above(r0)
        while l < r:
            if l & 1:
                self.X[l] = self.XA_map(self.X[l], a)
                self.A[l] = self.A_f(self.A[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.X[r] = self.XA_map(self.X[r], a)
                self.A[r] = self.A_f(self.A[r], a)
            l >>= 1
            r >>= 1
        self._calc_above(l0)
        self._calc_above(r0)
