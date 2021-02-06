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
集合内で `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\log n)$

- `kth_largest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\log n)$

- `prev_val(upper: int) -> int`  
集合内で `upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `next_val(lower: int) -> int`  
集合内で `lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `dump() -> List[int]`  
集合内の全ての要素を小さい順に返す。計算量 $O(n)$
