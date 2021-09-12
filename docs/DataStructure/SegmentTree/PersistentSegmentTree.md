---
title: 永続セグメント木
documentation_of: //DataStructure/SegmentTree/PersistentSegmentTree.py
---

## 概要
Segment Tree を永続化したデータ構造。定数倍が重い。

## 使い方
`PersistentSegmentTree(n: int, op: Callable[[T, T], T], e: T, root=None)`  
長さ $n$ の Persistent Segment Tree を構築する。計算量 $O(1)$

- `build(array: Sequence[Any]) -> None`  
Persistent Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> T`  
$i$ 番目の要素を返す。計算量 $O(1)$

- `update(i: int, val: T) -> PersistentSegmentTree`  
$i$ 番目の要素を `val` に更新した Persistent Segment Tree を返す。計算量 $O(\log n)$

- `all_fold() -> T`  
$[0, n)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

- `fold(l: int, r: int) -> T`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$
