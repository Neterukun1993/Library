---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/SegmentTree/LazySegmentTree.py
    title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment\
      \ Tree with Lazy Propagation)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_H.test.py
    title: TestCase/AOJ/DSL_2_H.test.py
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
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\n\n\
    \nclass RmQ_RAQ:\n    def __init__(self, n):\n        unitX = (1 << 31) - 1\n\
    \        unitA = 0\n        X_f = min\n        A_f = lambda a1, a2: a1 + a2\n\
    \        XA_map = lambda x, a: x + a\n        self.st = LazySegmentTree(n, unitX,\
    \ unitA, X_f, A_f, XA_map)\n        self.st.build([0] * n)\n\n    def build(self,\
    \ array):\n        self.st.build(array)\n\n    def __getitem__(self, i):\n   \
    \     return self.st[i]\n\n    def __setitem__(self, i, x):\n        self.st[i]\
    \ = x\n\n    def fold(self, l, r):\n        return self.st.fold(l, r)\n\n    def\
    \ apply(self, i, a):\n        self.st.apply(i, a)\n\n    def range_apply(self,\
    \ l, r, a):\n        self.st.range_apply(l, r, a)\n"
  dependsOn:
  - DataStructure/SegmentTree/LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure/SegmentTree/RmQ_RAQ.py
  requiredBy: []
  timestamp: '2022-04-24 23:38:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_H.test.py
documentation_of: DataStructure/SegmentTree/RmQ_RAQ.py
layout: document
title: RmQ_RAQ
---

## 概要
列に対する区間加算、区間最小値取得を $O(\log n)$ で行えるデータ構造。

## 使い方
`RmQ_RAQ(n: int)`  
区間更新、区間最小値取得が可能な長さ $n$ の配列を構築する。配列の初期値は `(1 << 31) - 1` である。計算量 $O(n)$

- `build(array: List[int]) -> None`  
配列を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, x: int) -> None`  
$i$ 番目の要素を `x` に更新する。計算量 $O(\log n)$

- `fold(l: int, r: int) -> T`  
$[l, r)$ 番目の区間最小値を返す。計算量 $O(\log n)$

- `apply(i: int, a: int) -> None`  
$i$ 番目の要素に `a` を加算する。計算量 $O(\log n)$

- `range_apply(l: int, r: int, a: int) -> None`  
$[l, r)$ 番目の要素に `a` を加算する。計算量 $O(\log n)$