---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RUQ.py
    title: RUQ
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class CommutativeDualSegmentTree:\n    def __init__(self, n, unitA, A_f):\n\
    \        self.n = n\n        self.unitA = unitA\n        self.A_f = A_f  # (A,\
    \ A) -> A\n        self.A = [unitA] * (n + n)\n\n    def __getitem__(self, i):\n\
    \        i += self.n\n        res = self.unitA\n        while i > 0:\n       \
    \     res = self.A_f(res, self.A[i])\n            i >>= 1\n        return res\n\
    \n    def __setitem__(self, i, val):\n        i += self.n\n        self.A[i] =\
    \ val\n\n    def apply(self, i, val):\n        i += self.n\n        self.A[i]\
    \ = self.A_f(self.A[i], val)\n\n    def range_apply(self, l, r, val):\n      \
    \  l += self.n\n        r += self.n\n        while l < r:\n            if l &\
    \ 1:\n                self.A[l] = self.A_f(self.A[l], val)\n                l\
    \ += 1\n            if r & 1:\n                r -= 1\n                self.A[r]\
    \ = self.A_f(self.A[r], val)\n            l >>= 1\n            r >>= 1\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/CommutativeDualSegmentTree.py
  requiredBy:
  - DataStructure/SegmentTree/RUQ.py
  timestamp: '2021-01-04 04:15:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/CommutativeDualSegmentTree.py
layout: document
title: "\u53EF\u63DB\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---
