---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_E.test.py
    title: TestCase/AOJ/DSL_2_E.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, n):\n        self.size =\
    \ n\n        self.bit = [0] * (self.size + 1)\n\n    def build(self, array):\n\
    \        for i, val in enumerate(array):\n            self.bit[i + 1] = val\n\
    \        for i in range(1, self.size):\n            if i + (i & -i) > self.size:\n\
    \                continue\n            self.bit[i] -= self.bit[i + (i & -i)]\n\
    \n    def __getitem__(self, i):\n        i = i + 1\n        s = 0\n        while\
    \ i <= self.size:\n            s += self.bit[i]\n            i += i & -i\n   \
    \     return s\n\n    def _add(self, i, val):\n        while i > 0:\n        \
    \    self.bit[i] += val\n            i -= i & -i\n\n    def add(self, l, r, val):\n\
    \        \"\"\"add value in range [l, r)\"\"\"\n        self._add(r, val)\n  \
    \      self._add(l, -val)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/RangeAddPointGet.py
  requiredBy: []
  timestamp: '2021-01-02 01:31:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_E.test.py
documentation_of: DataStructure/BinaryIndexedTree/RangeAddPointGet.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
---

## 概要
列に対する区間加算、一点取得を計算量 $O(\log n)$ で行えるデータ構造。

## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $O(n)$

- `build(array: Sequence[int]) -> None`  
Binary Indexed Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(\log n)$

- `add(l: int, r: int, val: int) -> None`  
$\lbrack l, r)$ 番目の要素に `val` を加える。計算量 $O(\log n)$
