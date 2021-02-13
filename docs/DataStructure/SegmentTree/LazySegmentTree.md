---
title: 遅延伝播セグメント木 (Segment Tree with Lazy Propagation)
documentation_of: //DataStructure/SegmentTree/LazySegmentTree.py
---

## 概要
列に対する区間作用、区間畳み込みを $O(\log n)$ で行えるデータ構造。作用素付きモノイドを要請する。

## 使い方
`LazySegmentTree(n: int, unitX: Any, unitA: Any, X_f: Callable[[Any, Any], Any], X_A: Callable[[Any, Any], Any], XA_map: Callable[[Any, Any], Any])`  
長さ `n` の Lazy Segment Tree を構築する。計算量 $O(n)$
それぞれの演算について、

  - 畳み込みの演算を二項演算 `f_X`、単位元 `unitX` として定義する。
  - 作用素同士の演算を二項演算 `f_A`、単位元 `unitA` として定義する。ただし `f_A(a, b)` のとき、`a` が作用される作用素、`b` が作用する作用素である。
  - 要素に対する作用を `XA_map` として定義する。ただし `XA_map(x, a)` のとき、`x` が作用される要素、`a` が作用する作用素である。

となる。

- `build(array: List[Any]) -> None`  
Lazy Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, x: Any) -> None`  
`i` 番目の要素を `x` に更新する。計算量 $O(\log n)$

- `fold(l: int, r: int) -> Any`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$

- `apply(i: int, a: Any) -> None`  
`i` 番目の要素に `a` を作用させる。計算量 $O(\log n)$

- `range_apply(l: int, r: int, a: Any) -> None`  
$[l, r)$ 番目の要素に `a` を作用させる。計算量 $O(\log n)$
