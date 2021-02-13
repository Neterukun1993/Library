---
title: 順序付き集合 (B-Tree)
documentation_of: //DataStructure/SortedSet/SortedSetBTree.py
---

## 概要
B-Tree による順序付き集合。

## 使い方
`SortedSetBTree(B_SIZE=512)`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $O(\log n)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $O(\log n)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log n)$

- `iterate(vl: int) -> Iterator[int]`  
`vl` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$
