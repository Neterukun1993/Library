---
title: 可換双対セグメント木
documentation_of: //DataStructure/SegmentTree/CommutativeDualSegmentTree.py
---

## 概要
列に対する区間作用、一点取得を $O(\log n)$ で行えるデータ構造。作用はモノイドに加えて可換性も要請するが、[双対セグメント木](https://neterukun1993.github.io/Library/DataStructure/SegmentTree/DualSegmentTree.py) よりも高速。

## 使い方
`CommutativeDualSegmentTree(n: int, unitA: Any, A_f: Callable[[Any, Any], Any])`  
長さ `n` の Commutative Dual Segment Tree を構築する。作用は演算子 `A_f`、単位元 `unitA` によって定義される。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, val: Any) -> None`  
`i` 番目の要素を `val` に更新する。計算量 $O(1)$

- `apply(i: int, val: Any) -> None`  
`i` 番目の要素に `val` を作用させる。計算量 $O(\log n)$

- `range_apply(l: int, r: int, val: Any) -> None`  
$[l, r)$ 番目の要素に `val` を作用させる。計算量 $O(\log n)$
