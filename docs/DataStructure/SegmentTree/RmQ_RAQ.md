---
title: RmQ_RAQ
documentation_of: //DataStructure/SegmentTree/RmQ_RAQ.py
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