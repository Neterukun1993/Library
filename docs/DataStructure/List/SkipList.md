---
title: 対数時間ランダムアクセス/挿入/削除可能リスト (スキップリスト)
documentation_of: //DataStructure/List/SkipList.py
---

## 概要
要素のランダムアクセス、挿入、削除を $\mathrm{expected}\ O(H + \log N)$ で行えるリスト。

## 使い方
`SkipList()`  
空のリストを作成する。ノードの高さを $H$ (デフォルトでは $H = 20$) としたときに、計算量 $O(H)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を代入する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `insert(i: int, val: int) -> None`  
$i$ 番目の位置に $val$ を挿入する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `delete(i: int) -> None`  
$i$ 番目の要素を削除する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `dump() -> List[int]`  
リストの要素を列挙した結果を返す。計算量 $O(N)$
