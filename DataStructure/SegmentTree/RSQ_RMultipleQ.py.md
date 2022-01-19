---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/SegmentTree/LazySegmentTree.py
    title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment\
      \ Tree with Lazy Propagation)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\n\n\
    \nMOD = 998244353\n\n\nclass RSQ_RMultipleQ(LazySegmentTree):\n    def __init__(self,\
    \ n):\n        unitX = 0\n        unitA = 1\n        X_f = lambda x1, x2: (x1\
    \ + x2) % MOD\n        A_f = lambda a1, a2: a1 * a2 % MOD\n        XA_map = lambda\
    \ x, a: x * a % MOD\n        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)"
  dependsOn:
  - DataStructure/SegmentTree/LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure/SegmentTree/RSQ_RMultipleQ.py
  requiredBy: []
  timestamp: '2021-10-03 01:03:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/RSQ_RMultipleQ.py
layout: document
title: RSQ_RMultipleQ
---

## 概要
列に対する区間乗算、区間和取得を $O(\log n)$ で行えるデータ構造。

## 使い方
`RSQ_RMultipleQ(n: int)`  
区間乗算、区間和取得が可能な長さ $n$ の配列を構築する。配列の初期値は $0$ である。計算量 $O(n)$

- `build(array: List[int]) -> None`  
配列を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を $998244353$ で割ったあまり返す。計算量 $O(\log n)$

- `__setitem__(i: int, x: int) -> None`  
$i$ 番目の要素を `x` に更新する。計算量 $O(\log n)$

- `fold(l: int, r: int) -> int`  
$[l, r)$ 番目の区間和を $998244353$ で割ったあまりを返す。計算量 $O(\log n)$

- `apply(i: int, a: int) -> None`  
$i$ 番目の要素を `a` 倍する。計算量 $O(\log n)$

- `range_apply(l: int, r: int, a: int) -> None`  
$[l, r)$ 番目の要素をそれぞれ `a` 倍する。計算量 $O(\log n)$