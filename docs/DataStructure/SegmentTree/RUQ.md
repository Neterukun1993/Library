---
title: RUQ
documentation_of: //DataStructure/SegmentTree/RUQ.py
---

## 概要
列に対する区間更新、一点取得を $O(\log n)$ で行えるデータ構造。

## 使い方
`RUQ(n: int)`  
区間更新が可能な長さ $n$ の配列を構築する。配列の初期値は $0$ である。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(\log n)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素を `val` に更新する。計算量 $O(1)$

- `apply(i: int, val: int) -> None`  
$i$ 番目の要素を `val` に更新する。`__setitem__` と同じ。計算量 $O(\log n)$

- `range_apply(l: int, r: int, val: int) -> None`  
$[l, r)$ 番目の要素を `val` に更新する。計算量 $O(\log n)$
