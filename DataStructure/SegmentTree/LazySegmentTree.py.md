---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RSQ_RUQ.py
    title: DataStructure/SegmentTree/RSQ_RUQ.py
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RmQ_RAQ.py
    title: DataStructure/SegmentTree/RmQ_RAQ.py
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RmQ_RUQ.py
    title: DataStructure/SegmentTree/RmQ_RUQ.py
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LazySegmentTree:\n    def __init__(self, n, unitX, unitA, X_f, A_f,\
    \ XA_map):\n        self.n = n\n        self.unitX = unitX\n        self.unitA\
    \ = unitA\n        self.X_f = X_f  # (X, X) -> X\n        self.A_f = A_f  # (A,\
    \ A) -> A\n        self.XA_map = XA_map  # (X, A) -> X\n        self.X = [unitX]\
    \ * (n + n)\n        self.A = [unitA] * (n + n)\n\n    def __getitem__(self, i):\n\
    \        i += self.n\n        self._propagate_above(i)\n        return self.X[i]\n\
    \n    def __setitem__(self, i, x):\n        i += self.n\n        self._propagate_above(i)\n\
    \        self.X[i] = x\n        self._calc_above(i)\n\n    def build(self, array):\n\
    \        for i, val in enumerate(array, self.n):\n            self.X[i] = val\n\
    \        for i in range(self.n - 1, 0, -1):\n            self.X[i] = self.X_f(self.X[i\
    \ << 1], self.X[i << 1 | 1])\n\n    def _calc_above(self, i):\n        while i\
    \ > 1:\n            i >>= 1\n            self.X[i] = self.X_f(self.X[i << 1],\
    \ self.X[i << 1 | 1])\n\n    def _propagate_above(self, i):\n        k = i >>\
    \ 1\n        H = k.bit_length() - 1\n        for h in range(H, -1, -1):\n    \
    \        i = k >> h\n            if self.A[i] == self.unitA:\n               \
    \ continue\n            self.X[i << 1] = self.XA_map(self.X[i << 1], self.A[i])\n\
    \            self.X[i << 1 | 1] = self.XA_map(self.X[i << 1 | 1], self.A[i])\n\
    \            self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])\n          \
    \  self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])\n            self.A[i]\
    \ = self.unitA\n\n    def fold(self, l, r):\n        l += self.n\n        r +=\
    \ self.n\n        l0, r0 = l // (l & -l), r // (r & -r) - 1\n        self._propagate_above(l0)\n\
    \        self._propagate_above(r0)\n        xl = self.unitX\n        xr = self.unitX\n\
    \        while l < r:\n            if l & 1:\n                xl = self.X_f(xl,\
    \ self.X[l])\n                l += 1\n            if r & 1:\n                r\
    \ -= 1\n                xr = self.X_f(self.X[r], xr)\n            l >>= 1\n  \
    \          r >>= 1\n        return self.X_f(xl, xr)\n\n    def apply(self, i,\
    \ a):\n        i += self.n\n        self._propagate_above(i)\n        self.X[i]\
    \ = self.XA_map(self.X[i], a)\n        self.A[i] = self.A_f(self.A[i], a)\n  \
    \      self._calc_above(i)\n\n    def range_apply(self, l, r, a):\n        l +=\
    \ self.n\n        r += self.n\n        l0, r0 = l // (l & -l), r // (r & -r) -\
    \ 1\n        self._propagate_above(l0)\n        self._propagate_above(r0)\n  \
    \      while l < r:\n            if l & 1:\n                self.X[l] = self.XA_map(self.X[l],\
    \ a)\n                self.A[l] = self.A_f(self.A[l], a)\n                l +=\
    \ 1\n            if r & 1:\n                r -= 1\n                self.X[r]\
    \ = self.XA_map(self.X[r], a)\n                self.A[r] = self.A_f(self.A[r],\
    \ a)\n            l >>= 1\n            r >>= 1\n        self._calc_above(l0)\n\
    \        self._calc_above(r0)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/LazySegmentTree.py
  requiredBy:
  - DataStructure/SegmentTree/RSQ_RUQ.py
  - DataStructure/SegmentTree/RmQ_RAQ.py
  - DataStructure/SegmentTree/RmQ_RUQ.py
  timestamp: '2021-01-02 17:11:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/LazySegmentTree.py
layout: document
title: "\u9045\u5EF6\u4F1D\u642C\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---
