---
title: Foldable Queue
documentation_of: //DataStructure/misc/FoldableQueue.py
---

## 概要
キューの操作をサポートし、キュー全体の畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群を要請する。

## 使い方
`SlidingWindowAggregation(op: Callable[[Any, Any], Any])`  
空のキューを構築する。`op` は畳み込みの二項演算。計算量 $O(1)$

- `__len__() -> int`  
キューの大きさを返す。計算量 $O(1)$

- `all_fold() -> Any`  
キュー全体の畳み込み結果を返す。計算量 $O(1)$

- `append(val: Any) -> None`  
キューの末尾に要素 `val` を追加する。計算量 $O(1)$

- `popleft() -> Any`  
キューの先頭要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$
