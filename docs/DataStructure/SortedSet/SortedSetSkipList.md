---
title: 順序付き集合 (スキップリスト)
documentation_of: //DataStructure/SortedSet/SortedSetSkipList.py
---

## 概要
スキップリストによる順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetSkipList()`  
空の順序付き集合を作成する。ノードの高さを $H$ (デフォルトでは $H = 20$) としたときに、計算量 $O(H)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$。イテレーション1回の計算量 $O(1)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $\mathrm{expected}\ O(H + \log N)$。イテレーション1回の計算量 $O(1)$

- `next_val(lower: int) -> int`  
`lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。 $\mathrm{expected}\ O(H + \log N)$

- `prev_val(upper: int) -> int`  
`upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。 $\mathrm{expected}\ O(H + \log N)$
