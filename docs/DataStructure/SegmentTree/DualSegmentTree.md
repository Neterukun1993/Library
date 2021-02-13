---
title: 双対セグメント木 (Dual Segment Tree)
documentation_of: //DataStructure/SegmentTree/DualSegmentTree.py
---

## 概要
列に対する区間作用、一点取得を $O(\log n)$ で行えるデータ構造。作用はモノイドを要請する。

## 使い方
`DualSegmentTree(n: int, unitA: Any, A_f: Callable[[Any, Any], Any])`  
長さ `n` の Dual Segment Tree を構築する。作用は演算子 `A_f`、単位元 `unitA` によって定義される。`A_f(a, b)` のとき、`a` が作用される要素、`b` が作用する要素となることに注意。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, val: Any) -> None`  
`i` 番目の要素を `val` に更新する。計算量 $O(\log n)$

- `apply(i: int, val: Any) -> None`  
`i` 番目の要素に `val` を作用させる。計算量 $O(\log n)$

- `range_apply(l: int, r: int, val: Any) -> None`  
$[l, r)$ 番目の要素に `val` を作用させる。計算量 $O(\log n)$
