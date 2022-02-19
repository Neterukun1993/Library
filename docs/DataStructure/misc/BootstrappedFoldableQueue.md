---　
title: 永続 Sliding Window Aggregation
documentation_of: //DataStructure/misc/BootstrappedFoldableQueue.py
---

## 概要
Sliding Window Aggregation を永続化したデータ構造。

## 使い方
`BootstrappedFoldableQueue[T](op: Callable[[T, T], T])`  
空のキューを構築する。`op` は畳み込みの二項演算。計算量 $O(1)$

- `__len__() -> int`  
キューの大きさを返す。計算量 $O(1)$

- `all_fold() -> T`  
キュー全体の畳み込み結果を返す。計算量 $O(1)$

- `snoc(val: T) -> BootstrappedFoldableQueue[T]`  
キューの末尾に要素 `val` を追加する。計算量 $O(1)$

- `head() -> T`  
キューの先頭の要素を返す。計算量 $O(1)$

- `tail() -> BootstrappedFoldableQueue[T]`  
キューの先頭要素を削除したキューを返す。計算量 $\mathrm{amortized}\ O(1)$
