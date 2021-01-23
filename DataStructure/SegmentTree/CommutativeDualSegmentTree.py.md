---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\RUQ.py
    title: RUQ
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
  code: "class CommutativeDualSegmentTree:\r\n    def __init__(self, n, unitA, A_f):\r\
    \n        self.n = n\r\n        self.unitA = unitA\r\n        self.A_f = A_f \
    \ # (A, A) -> A\r\n        self.A = [unitA] * (n + n)\r\n\r\n    def __getitem__(self,\
    \ i):\r\n        i += self.n\r\n        res = self.unitA\r\n        while i >\
    \ 0:\r\n            res = self.A_f(res, self.A[i])\r\n            i >>= 1\r\n\
    \        return res\r\n\r\n    def __setitem__(self, i, val):\r\n        i +=\
    \ self.n\r\n        self.A[i] = val\r\n\r\n    def apply(self, i, val):\r\n  \
    \      i += self.n\r\n        self.A[i] = self.A_f(self.A[i], val)\r\n\r\n   \
    \ def range_apply(self, l, r, val):\r\n        l += self.n\r\n        r += self.n\r\
    \n        while l < r:\r\n            if l & 1:\r\n                self.A[l] =\
    \ self.A_f(self.A[l], val)\r\n                l += 1\r\n            if r & 1:\r\
    \n                r -= 1\r\n                self.A[r] = self.A_f(self.A[r], val)\r\
    \n            l >>= 1\r\n            r >>= 1\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\CommutativeDualSegmentTree.py
  requiredBy:
  - DataStructure\SegmentTree\RUQ.py
  timestamp: '2021-01-04 04:15:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\SegmentTree\CommutativeDualSegmentTree.py
layout: document
title: "\u53EF\u63DB\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---
