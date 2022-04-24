---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/SegmentTree/CommutativeDualSegmentTree.py
    title: "\u53EF\u63DB\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Commutative\
      \ Dual Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
    title: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.CommutativeDualSegmentTree import CommutativeDualSegmentTree\n\
    \n\nclass RUQ:\n    def __init__(self, n):\n        unitA = (0, 0)\n        A_f\
    \ = lambda a1, a2: a2 if a2 > a1 else a1\n        self.st = CommutativeDualSegmentTree(n,\
    \ unitA, A_f)\n        self.cnt = 1\n\n    def __getitem__(self, i):\n       \
    \ return self.st[i][1]\n\n    def __setitem__(self, i, val):\n        self.cnt\
    \ += 1\n        self.st[i] = (self.cnt, val)\n\n    def apply(self, i, val):\n\
    \        self.cnt += 1\n        self.st.apply(i, (self.cnt, val))\n\n    def range_apply(self,\
    \ l, r, val):\n        self.cnt += 1\n        self.st.range_apply(l, r, (self.cnt,\
    \ val))\n"
  dependsOn:
  - DataStructure/SegmentTree/CommutativeDualSegmentTree.py
  isVerificationFile: false
  path: DataStructure/SegmentTree/RUQ.py
  requiredBy: []
  timestamp: '2022-04-24 23:38:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
documentation_of: DataStructure/SegmentTree/RUQ.py
layout: document
title: RUQ
---

## 概要
列に対する区間更新、一点取得を $O(\log n)$ で行えるデータ構造。

## 使い方
`RUQ(n: int)`  
区間更新が可能な長さ $n$ の配列を構築する。配列の初期値は $0$ である。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素を `val` に更新する。計算量 $O(1)$

- `apply(i: int, val: int) -> None`  
$i$ 番目の要素を `val` に更新する。`__setitem__` と同じ。計算量 $O(\log n)$

- `range_apply(l: int, r: int, val: int) -> None`  
$[l, r)$ 番目の要素を `val` に更新する。計算量 $O(\log n)$
