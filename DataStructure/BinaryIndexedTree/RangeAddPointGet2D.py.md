---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_5_B.BIT.test.py
    title: TestCase/AOJ/DSL_5_B.BIT.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, h, w):\n        self.h =\
    \ h\n        self.w = w\n        self.bit = [[0] * (self.w + 1) for _ in range(self.h\
    \ + 1)]\n\n    def get(self, i, j):\n        j0 = j\n        i = i + 1\n     \
    \   s = 0\n        while i <= self.h:\n            j = j0 + 1\n            while\
    \ j <= self.w:\n                s += self.bit[i][j]\n                j += j &\
    \ -j\n            i += i & -i\n        return s\n\n    def _add(self, i, j, val):\n\
    \        j0 = j\n        while i > 0:\n            j = j0\n            while j\
    \ > 0:\n                self.bit[i][j] += val\n                j -= j & -j\n \
    \           i -= i & -i\n\n    def add(self, hl, hr, wl, wr, val):\n        \"\
    \"\"add value in range [l, r)\"\"\"\n        self._add(hl, wl, val)\n        self._add(hr,\
    \ wl, -val)\n        self._add(hl, wr, -val)\n        self._add(hr, wr, val)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/RangeAddPointGet2D.py
  requiredBy: []
  timestamp: '2021-05-08 19:01:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_5_B.BIT.test.py
documentation_of: DataStructure/BinaryIndexedTree/RangeAddPointGet2D.py
layout: document
title: "\u77E9\u5F62\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
---

## 概要
二次元配列に対して矩形範囲加算、一点取得を計算量 $O(\log h\log w)$ で行えるデータ構造。

## 使い方
`BinaryIndexedTree(h: int, w: int)`  
大きさ $h × w$ の二次元 Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $O(hw)$

- `get(i: int, j: int) -> int`  
$i$ 行 $j$ 列目の要素を返す。計算量$O(\log h\log w)$

- `add(hl: int, hr: int, wl: int, wr: int, val: int) -> None`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素に `val` を加える。計算量 $O(\log h\log w)$
