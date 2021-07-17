---
title: 一点加算・区間和取得
documentation_of: //DataStructure/BinaryIndexedTree/PointAddRangeSum.py
---

## 概要
列に対する一点加算、区間和取得を計算量 $O(\log n)$ で行えるデータ構造。

## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $O(n)$

- `build(array: Sequence[int]) -> None`  
Binary Indexed Tree を配列 `array` で初期化する。計算量 $O(n)$

- `add(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を加える。計算量 $O(\log n)$

- `sum(l: int, r: int) -> int`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(\log n)$

- `bisect_left(val: int) -> int`  
$\lbrack 0, r)$ 番目の要素の総和が `val` 以上となる最小の $r$ を返す。そのような $r$ が存在しない場合は $n + 1$ を返す。計算量 $O(\log n)$
