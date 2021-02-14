---
title: 永続Binary Indexed Tree
documentation_of: //DataStructure/BinaryIndexedTree/PersistentBinaryIndexedTree.py
---

## 概要
Binary Indexed Tree を永続化したデータ構造。定数倍が重い。

## 使い方
`PersistentBinaryIndexedTree(n: int, root=None)`  
長さ `n` の Persistent Binary Indexed Tree を構築する。計算量 $O(1)$

- `build(array: Sequence[int]) -> None`  
Persistent Binary Indexed Tree を `array` で初期化する。計算量 $O(n)$

- `add(i: int, val: int) -> PersistentBinaryIndexedTree`  
`i` 番目の要素に `val` を加えた Persistent Binry Indexed Tree を返す。計算量 $O(\log n)$

- `sum(l: int, r: int) -> int`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(\log n)$
