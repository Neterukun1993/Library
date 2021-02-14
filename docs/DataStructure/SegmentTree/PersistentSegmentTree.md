---
title: 永続セグメント木
documentation_of: //DataStructure/SegmentTree/PersistentSegmentTree.py
---

## 概要
Segment Tree を永続化したデータ構造。定数倍が重い。

## 使い方
`PersistentSegmentTree(n: int, op: Callable[[Any, Any], Any], e: Any, root=None)`  
長さ `n` の Persistent Segment Tree を構築する。計算量 $O(1)$

- `build(array: Sequence[Any]) -> None`  
Persistent Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(1)$

- `update(i: int, val: Any) -> PersistentSegmentTree`  
`i` 番目の要素を `val` に更新した Persistent Segment Tree を返す。計算量 $O(\log n)$

- `all_fold() -> Any`  
$[0, n)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

- `fold(l: int, r: int) -> Any`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$
