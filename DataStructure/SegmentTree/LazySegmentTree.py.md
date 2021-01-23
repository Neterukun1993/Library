---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\RSQ_RUQ.py
    title: RSQ_RUQ
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\RmQ_RAQ.py
    title: RmQ_RAQ
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\RmQ_RUQ.py
    title: RmQ_RUQ
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LazySegmentTree:\r\n    def __init__(self, n, unitX, unitA, X_f, A_f,\
    \ XA_map):\r\n        self.n = n\r\n        self.unitX = unitX\r\n        self.unitA\
    \ = unitA\r\n        self.X_f = X_f  # (X, X) -> X\r\n        self.A_f = A_f \
    \ # (A, A) -> A\r\n        self.XA_map = XA_map  # (X, A) -> X\r\n        self.X\
    \ = [unitX] * (n + n)\r\n        self.A = [unitA] * (n + n)\r\n\r\n    def __getitem__(self,\
    \ i):\r\n        i += self.n\r\n        self._propagate_above(i)\r\n        return\
    \ self.X[i]\r\n\r\n    def __setitem__(self, i, x):\r\n        i += self.n\r\n\
    \        self._propagate_above(i)\r\n        self.X[i] = x\r\n        self._calc_above(i)\r\
    \n\r\n    def build(self, array):\r\n        for i, val in enumerate(array, self.n):\r\
    \n            self.X[i] = val\r\n        for i in range(self.n - 1, 0, -1):\r\n\
    \            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])\r\n\r\n\
    \    def _calc_above(self, i):\r\n        while i > 1:\r\n            i >>= 1\r\
    \n            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])\r\n\r\n\
    \    def _propagate_above(self, i):\r\n        k = i >> 1\r\n        H = k.bit_length()\
    \ - 1\r\n        for h in range(H, -1, -1):\r\n            i = k >> h\r\n    \
    \        if self.A[i] == self.unitA:\r\n                continue\r\n         \
    \   self.X[i << 1] = self.XA_map(self.X[i << 1], self.A[i])\r\n            self.X[i\
    \ << 1 | 1] = self.XA_map(self.X[i << 1 | 1], self.A[i])\r\n            self.A[i\
    \ << 1] = self.A_f(self.A[i << 1], self.A[i])\r\n            self.A[i << 1 | 1]\
    \ = self.A_f(self.A[i << 1 | 1], self.A[i])\r\n            self.A[i] = self.unitA\r\
    \n\r\n    def fold(self, l, r):\r\n        l += self.n\r\n        r += self.n\r\
    \n        l0, r0 = l // (l & -l), r // (r & -r) - 1\r\n        self._propagate_above(l0)\r\
    \n        self._propagate_above(r0)\r\n        xl = self.unitX\r\n        xr =\
    \ self.unitX\r\n        while l < r:\r\n            if l & 1:\r\n            \
    \    xl = self.X_f(xl, self.X[l])\r\n                l += 1\r\n            if\
    \ r & 1:\r\n                r -= 1\r\n                xr = self.X_f(self.X[r],\
    \ xr)\r\n            l >>= 1\r\n            r >>= 1\r\n        return self.X_f(xl,\
    \ xr)\r\n\r\n    def apply(self, i, a):\r\n        i += self.n\r\n        self._propagate_above(i)\r\
    \n        self.X[i] = self.XA_map(self.X[i], a)\r\n        self.A[i] = self.A_f(self.A[i],\
    \ a)\r\n        self._calc_above(i)\r\n\r\n    def range_apply(self, l, r, a):\r\
    \n        l += self.n\r\n        r += self.n\r\n        l0, r0 = l // (l & -l),\
    \ r // (r & -r) - 1\r\n        self._propagate_above(l0)\r\n        self._propagate_above(r0)\r\
    \n        while l < r:\r\n            if l & 1:\r\n                self.X[l] =\
    \ self.XA_map(self.X[l], a)\r\n                self.A[l] = self.A_f(self.A[l],\
    \ a)\r\n                l += 1\r\n            if r & 1:\r\n                r -=\
    \ 1\r\n                self.X[r] = self.XA_map(self.X[r], a)\r\n             \
    \   self.A[r] = self.A_f(self.A[r], a)\r\n            l >>= 1\r\n            r\
    \ >>= 1\r\n        self._calc_above(l0)\r\n        self._calc_above(r0)\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\LazySegmentTree.py
  requiredBy:
  - DataStructure\SegmentTree\RmQ_RAQ.py
  - DataStructure\SegmentTree\RmQ_RUQ.py
  - DataStructure\SegmentTree\RSQ_RUQ.py
  timestamp: '2021-01-02 17:11:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\SegmentTree\LazySegmentTree.py
layout: document
title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree\
  \ with Lazy Propagation)"
---
