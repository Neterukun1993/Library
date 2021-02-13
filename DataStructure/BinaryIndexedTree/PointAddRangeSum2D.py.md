---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/0560.BIT.test.py
    title: TestCase/AOJ/0560.BIT.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, h, w):\n        self.h =\
    \ h\n        self.w = w\n        self.bit = [[0] * (self.w + 1) for _ in range(self.h\
    \ + 1)]\n\n    def add(self, i, j, val):\n        hi, wj = i, j\n        i = hi\
    \ + 1\n        while i <= self.h:\n            j = wj + 1\n            while j\
    \ <= self.w:\n                self.bit[i][j] += val\n                j += j &\
    \ -j\n            i += i & -i\n\n    def _sum(self, i, j):\n        s, hi, wj\
    \ = 0, i, j\n        i = hi\n        while i > 0:\n            j = wj\n      \
    \      while j > 0:\n                s += self.bit[i][j]\n                j -=\
    \ j & -j\n            i -= i & -i\n        return s\n\n    def sum(self, hl, hr,\
    \ wl, wr):\n        \"\"\"sum of values in range [hl, hr) * [wl, wr)\"\"\"\n \
    \       return self._sum(hr, wr) - self._sum(hl, wr) \\\n               - self._sum(hr,\
    \ wl) + self._sum(hl, wl)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/PointAddRangeSum2D.py
  requiredBy: []
  timestamp: '2021-01-02 15:25:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/0560.BIT.test.py
documentation_of: DataStructure/BinaryIndexedTree/PointAddRangeSum2D.py
layout: document
title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
---

## 使い方
`BinaryIndexedTree(h: int, w: int)`  
大きさが $h × w$ の二次元 Binary Indexed Tree を構築する。初期値はすべて `0` である。計算量 $O(hw)$

- `add(i: int, j: int, val: int) -> None`  
`i` 番目の行、`j` 番目の列の要素に `val` を加える。計算量 $O(\log h\log w)$

- `sum(hl: int, hr: int, wl: int, wr: int) -> int`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $O(\log h\log w)$
