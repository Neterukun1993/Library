---
title: 順序付き集合 (Binary Indexed Tree)
documentation_of: //DataStructure/SortedSet/SortedSetBIT.py
---
## 概要
Binary Indexed Tree による順序付き集合。集合に属する可能性のある要素を、あらかじめ与える必要があることに注意。

## 使い方
`SortedSetBIT(cands: Iterable[int])`  
`cands` 内の要素を元として含むことが可能な、空の順序付き集合を作成する。`n = len(cands)` とすると、計算量 $O(n \log n)$

- `__contains__(val: int) -> bool`  
要素 `val` が集合に属しているかどうかを返す。計算量 $O(\log n)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `add(val: int) -> bool`  
要素 `val` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。`val` が `cands` の要素ではない場合は例外 `KeyError` が発生するので注意。計算量 $O(\log n)$

- `remove(val: int) -> bool`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log n)$

- `count(vl: int, vr: int) -> int`  
集合内の `vl` 以上かつ `vr` 未満である要素の数を返す。計算量 $O(\log n)$

- `kth_smallest(k: int) -> int`  
集合の中で `k` 番目 (0-indexed) に小さい値を返す。計算量 $O(\log n)$

- `kth_smallest(k: int) -> int`  
集合の中で `k` 番目 (0-indexed) に大きい値を返す。計算量 $O(\log n)$
