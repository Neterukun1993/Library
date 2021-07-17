---
title: 区間加算・一点取得
documentation_of: //DataStructure/BinaryIndexedTree/RangeAddPointGet.py
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
