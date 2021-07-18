---
title: 永続配列
documentation_of: //DataStructure/misc/PersistentArray.py
---

## 概要
永続化された配列。つまり、代入操作前と後のバージョンを常に保持し、全バージョンに対するアクセスと更新が可能な配列。

## 使い方
`init_persistent_array(array: Sequence[Any]) -> PersistentArray`  
長さ $n$ の配列 `array` の永続配列を返す。計算量 $O(n \log n)$

永続配列のメソッド `set` と `get` によって、全バージョンに対するアクセスと更新が可能。

- `set(i: int, val: Any) -> PersistentArray`  
$i$ 番目の要素に `val` を代入した永続配列を返す。計算量 $O(\log n)$

- `get(i: int) -> Any`  
$i$ 番目の要素を返す。計算量 $O(\log n)$
