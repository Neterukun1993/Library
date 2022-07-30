---
title: 対数時間ランダムアクセス/挿入/削除可能リスト (スプレー木)
documentation_of: //DataStructure/List/SplayTreeList.py
---
## 概要
要素のランダムアクセス、挿入、削除を $\mathrm{amortized}\ O(\log N)$ で行えるリスト。

## 使い方
`SplayTreeList()`  
空のリストを作成する。計算量 $O(1)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $\mathrm{amortized}\ O(\log N)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を代入する。計算量 $\mathrm{amortized}\ O(\log N)$

- `__len__() -> int`  
リストの長さを返す。計算量 $O(1)$

- `insert(i: int, val: int) -> None`  
$i$ 番目の位置に `val` を挿入する。計算量 $\mathrm{amortized}\ O(H + \log N)$

- `delete(i: int) -> None`  
$i$ 番目の要素を削除する。計算量 $\mathrm{amortized}\ O(\log N)$
