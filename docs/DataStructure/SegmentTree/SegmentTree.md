---
title: セグメント木 (Segment Tree)
documentation_of: //DataStructure/SegmentTree/SegmentTree.py
---
## 概要
列に対する一点更新、区間畳み込みを $O(\log n)$ で行えるデータ構造。畳み込みはモノイドを要請する。

## 使い方
`SegmentTree(n: int, op: Callable[[Any, Any], Any], e: Any)`  
長さ `n` の Segment Tree を構築する。畳み込み演算は二項演算 `op`、単位元 `e` によって定義される。計算量 $O(n)$

- `build(array: List[Any]) -> None`  
Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(1)$

- `__setitem__(i: int, val: Any) -> None`  
`i` 番目の要素を `val` に更新する。計算量 $O(\log n)$

- `all_fold() -> Any`  
$[0, n)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

- `fold(l: int, r: int) -> Any`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$
