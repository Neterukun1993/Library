---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/0098.test.py
    title: TestCase/AOJ/0098.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/0560.test.py
    title: TestCase/AOJ/0560.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class AccumulateSum2D:\n    def __init__(self, matrix):\n        self.h =\
    \ len(matrix)\n        self.w = len(matrix[0])\n        self.cumsum = [[0] * (self.w\
    \ + 1) for _ in range(self.h + 1)]\n\n        for i in range(self.h):\n      \
    \      for j in range(self.w):\n                self.cumsum[i + 1][j + 1] = self.cumsum[i\
    \ + 1][j] + matrix[i][j]\n        for i in range(self.h):\n            for j in\
    \ range(self.w):\n                self.cumsum[i + 1][j + 1] += self.cumsum[i][j\
    \ + 1]\n\n    def sum(self, hl, hr, wl, wr):\n        \"\"\"sum of values in range\
    \ [hl, hr) * [wl, wr)\"\"\"\n        return (self.cumsum[hr][wr] + self.cumsum[hl][wl]\n\
    \                - self.cumsum[hr][wl] - self.cumsum[hl][wr])\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/AccumulateSum2D.py
  requiredBy: []
  timestamp: '2021-01-02 00:00:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/0098.test.py
  - TestCase/AOJ/0560.test.py
documentation_of: DataStructure/AccumulateSum/AccumulateSum2D.py
layout: document
title: "\u4E8C\u6B21\u5143\u7D2F\u7A4D\u548C"
---

## 使い方
`AccumulateSum2D(matrix: List[List[Any])`  
`matrix` の二次元累積和を構築する。`matrix` のサイズを $h × w$ としたとき、計算量 $O(hw)$

- `sum(hl: int, hr: int, wl: int, wr: int) -> Any`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $O(1)$
