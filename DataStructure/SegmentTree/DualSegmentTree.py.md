---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_D.test.py
    title: TestCase\AOJ\DSL_2_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DualSegmentTree:\r\n    def __init__(self, n, unitA, A_f):\r\n    \
    \    self.n = n\r\n        self.unitA = unitA\r\n        self.A_f = A_f  # (A,\
    \ A) -> A\r\n        self.A = [unitA] * (n + n)\r\n\r\n    def __getitem__(self,\
    \ i):\r\n        i += self.n\r\n        self._propagate_above(i)\r\n        return\
    \ self.A[i]\r\n\r\n    def __setitem__(self, i, val):\r\n        i += self.n\r\
    \n        self._propagate_above(i)\r\n        self.A[i] = val\r\n\r\n    def _propagate_above(self,\
    \ i):\r\n        k = i >> 1\r\n        H = k.bit_length() - 1\r\n        for h\
    \ in range(H, -1, -1):\r\n            i = k >> h\r\n            if self.A[i] ==\
    \ self.unitA:\r\n                continue\r\n            self.A[i << 1 | 0] =\
    \ self.A_f(self.A[i << 1 | 0], self.A[i])\r\n            self.A[i << 1 | 1] =\
    \ self.A_f(self.A[i << 1 | 1], self.A[i])\r\n            self.A[i] = self.unitA\r\
    \n\r\n    def apply(self, i, val):\r\n        i += self.n\r\n        self._propagate_above(i)\r\
    \n        self.A[i] = self.A_f(self.A[i], val)\r\n\r\n    def range_apply(self,\
    \ l, r, val):\r\n        l += self.n\r\n        r += self.n\r\n        l0, r0\
    \ = l // (l & -l), r // (r & -r) - 1\r\n        self._propagate_above(l0)\r\n\
    \        self._propagate_above(r0)\r\n        while l < r:\r\n            if l\
    \ & 1:\r\n                self.A[l] = self.A_f(self.A[l], val)\r\n           \
    \     l += 1\r\n            if r & 1:\r\n                r -= 1\r\n          \
    \      self.A[r] = self.A_f(self.A[r], val)\r\n            l >>= 1\r\n       \
    \     r >>= 1\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\DualSegmentTree.py
  requiredBy: []
  timestamp: '2021-01-02 05:02:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_D.test.py
documentation_of: DataStructure\SegmentTree\DualSegmentTree.py
layout: document
title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual Segment Tree)"
---
