---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_D.test.py
    title: TestCase/AOJ/DSL_2_D.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DualSegmentTree:\n    def __init__(self, n, unitA, A_f):\n        self.n\
    \ = n\n        self.unitA = unitA\n        self.A_f = A_f  # (A, A) -> A\n   \
    \     self.A = [unitA] * (n + n)\n\n    def __getitem__(self, i):\n        i +=\
    \ self.n\n        self._propagate_above(i)\n        return self.A[i]\n\n    def\
    \ __setitem__(self, i, val):\n        i += self.n\n        self._propagate_above(i)\n\
    \        self.A[i] = val\n\n    def _propagate_above(self, i):\n        k = i\
    \ >> 1\n        H = k.bit_length() - 1\n        for h in range(H, -1, -1):\n \
    \           i = k >> h\n            if self.A[i] == self.unitA:\n            \
    \    continue\n            self.A[i << 1 | 0] = self.A_f(self.A[i << 1 | 0], self.A[i])\n\
    \            self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])\n  \
    \          self.A[i] = self.unitA\n\n    def apply(self, i, val):\n        i +=\
    \ self.n\n        self._propagate_above(i)\n        self.A[i] = self.A_f(self.A[i],\
    \ val)\n\n    def range_apply(self, l, r, val):\n        l += self.n\n       \
    \ r += self.n\n        l0, r0 = l // (l & -l), r // (r & -r) - 1\n        self._propagate_above(l0)\n\
    \        self._propagate_above(r0)\n        while l < r:\n            if l & 1:\n\
    \                self.A[l] = self.A_f(self.A[l], val)\n                l += 1\n\
    \            if r & 1:\n                r -= 1\n                self.A[r] = self.A_f(self.A[r],\
    \ val)\n            l >>= 1\n            r >>= 1\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/DualSegmentTree.py
  requiredBy: []
  timestamp: '2021-01-02 05:02:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_D.test.py
documentation_of: DataStructure/SegmentTree/DualSegmentTree.py
layout: document
title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---
