---
title: 区間加算・区間和取得
documentation_of: //DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
---

## 使い方
`BinaryIndexedTree(n: int)`  
長さ `n` の Binary Indexed Tree を構築する。初期値はすべて `0` である。計算量 $O(n)$

- `add(l: int, r: int, val: int) -> None`  
$\lbrack l, r)$ 番目の要素に `val` を加える。計算量 $O(\log n)$

- `sum(l: int, r: int) -> int`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(\log n)$
