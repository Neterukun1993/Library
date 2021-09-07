---
title: 順序付き集合 (スケープゴート木)
documentation_of: //DataStructure/SortedSet/SortedSetScapegoatTree.py
---

## 概要
スケープゴート木による順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetScapegoatTree()`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $O(\log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $N$ 要素のイテレーションの計算量 $O(N)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $\mathrm{amortized}\ O(\log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $\mathrm{amortized}\ O(\log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $k$ 要素のイテレーションの計算量 $O(k + \log N)$
