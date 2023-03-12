---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RMaxQ_RAQ.py
    title: DataStructure/SegmentTree/RMaxQ_RAQ.py
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RMaxQ_RUQ.py
    title: DataStructure/SegmentTree/RMaxQ_RUQ.py
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RSQ_RMultipleQ.py
    title: RSQ_RMultipleQ
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RSQ_RUQ.py
    title: RSQ_RUQ
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RmQ_RAQ.py
    title: RmQ_RAQ
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RmQ_RUQ.py
    title: RmQ_RUQ
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LazySegmentTree:\n    def __init__(self, n, unitX, unitA, X_f, A_f,\
    \ XA_map):\n        self.n = n\n        self.unitX = unitX\n        self.unitA\
    \ = unitA\n        self.X_f = X_f  # (X, X) -> X\n        self.A_f = A_f  # (A,\
    \ A) -> A\n        self.XA_map = XA_map  # (X, A) -> X\n        self.X = [unitX]\
    \ * (n + n)\n        self.A = [unitA] * (n + n)\n\n    def __getitem__(self, i):\n\
    \        i += self.n\n        self._propagate_above(i)\n        return self.X[i]\n\
    \n    def __setitem__(self, i, x):\n        i += self.n\n        self._propagate_above(i)\n\
    \        self.X[i] = x\n        self._calc_above(i)\n\n    def build(self, array):\n\
    \        for i, val in enumerate(array, self.n):\n            self.X[i] = val\n\
    \        for i in range(self.n - 1, 0, -1):\n            self.X[i] = self.X_f(self.X[i\
    \ << 1], self.X[i << 1 | 1])\n\n    def _calc_above(self, i):\n        while i\
    \ > 1:\n            i >>= 1\n            self.X[i] = self.X_f(self.X[i << 1],\
    \ self.X[i << 1 | 1])\n\n    def _propagate_above(self, i):\n        k = i >>\
    \ 1\n        H = k.bit_length() - 1\n        for h in range(H, -1, -1):\n    \
    \        i = k >> h\n            if self.A[i] == self.unitA:\n               \
    \ continue\n            self.X[i << 1] = self.XA_map(self.X[i << 1], self.A[i])\n\
    \            self.X[i << 1 | 1] = self.XA_map(self.X[i << 1 | 1], self.A[i])\n\
    \            self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])\n          \
    \  self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])\n            self.A[i]\
    \ = self.unitA\n\n    def fold(self, l, r):\n        l += self.n\n        r +=\
    \ self.n\n        l0, r0 = l // (l & -l), r // (r & -r) - 1\n        self._propagate_above(l0)\n\
    \        self._propagate_above(r0)\n        xl = self.unitX\n        xr = self.unitX\n\
    \        while l < r:\n            if l & 1:\n                xl = self.X_f(xl,\
    \ self.X[l])\n                l += 1\n            if r & 1:\n                r\
    \ -= 1\n                xr = self.X_f(self.X[r], xr)\n            l >>= 1\n  \
    \          r >>= 1\n        return self.X_f(xl, xr)\n\n    def apply(self, i,\
    \ a):\n        i += self.n\n        self._propagate_above(i)\n        self.X[i]\
    \ = self.XA_map(self.X[i], a)\n        self.A[i] = self.A_f(self.A[i], a)\n  \
    \      self._calc_above(i)\n\n    def range_apply(self, l, r, a):\n        l +=\
    \ self.n\n        r += self.n\n        l0, r0 = l // (l & -l), r // (r & -r) -\
    \ 1\n        self._propagate_above(l0)\n        self._propagate_above(r0)\n  \
    \      while l < r:\n            if l & 1:\n                self.X[l] = self.XA_map(self.X[l],\
    \ a)\n                self.A[l] = self.A_f(self.A[l], a)\n                l +=\
    \ 1\n            if r & 1:\n                r -= 1\n                self.X[r]\
    \ = self.XA_map(self.X[r], a)\n                self.A[r] = self.A_f(self.A[r],\
    \ a)\n            l >>= 1\n            r >>= 1\n        self._calc_above(l0)\n\
    \        self._calc_above(r0)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/LazySegmentTree.py
  requiredBy:
  - DataStructure/SegmentTree/RMaxQ_RUQ.py
  - DataStructure/SegmentTree/RmQ_RAQ.py
  - DataStructure/SegmentTree/RSQ_RMultipleQ.py
  - DataStructure/SegmentTree/RMaxQ_RAQ.py
  - DataStructure/SegmentTree/RSQ_RUQ.py
  - DataStructure/SegmentTree/RmQ_RUQ.py
  timestamp: '2021-01-02 17:11:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/LazySegmentTree.py
layout: document
title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree\
  \ with Lazy Propagation)"
---

## 概要
列に対する区間作用、区間畳み込みを $O(\log n)$ で行えるデータ構造。作用素付きモノイドを要請する。

## 使い方
`LazySegmentTree(n: int, unitX: T, unitA: U, X_f: Callable[[T, T], T], X_A: Callable[[U, U], U], XA_map: Callable[[T, U], T])`  
長さ $n$ の Lazy Segment Tree を構築する。計算量 $O(n)$
それぞれの演算について、

  - 畳み込みの演算を二項演算 `f_X`、単位元 `unitX` として定義する。
  - 作用素同士の演算を二項演算 `f_A`、単位元 `unitA` として定義する。ただし `f_A(a, b)` のとき、`a` が作用される作用素、`b` が作用する作用素である。
  - 要素に対する作用を `XA_map` として定義する。ただし `XA_map(x, a)` のとき、`x` が作用される要素、`a` が作用する作用素である。

となる。

- `build(array: List[T]) -> None`  
Lazy Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> T`  
$i$ 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, x: T) -> None`  
$i$ 番目の要素を `x` に更新する。計算量 $O(\log n)$

- `fold(l: int, r: int) -> T`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$

- `apply(i: int, a: U) -> None`  
$i$ 番目の要素に `a` を作用させる。計算量 $O(\log n)$

- `range_apply(l: int, r: int, a: U) -> None`  
$[l, r)$ 番目の要素に `a` を作用させる。計算量 $O(\log n)$
