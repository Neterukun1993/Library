---
title: 木のハッシュ (木の同型判定)
documentation_of: //Graph/Tree/treehash.py
---

## 概要
木のハッシュを求めるアルゴリズム。

## 使い方
`treehash(tree: Sequence[Iterable[int]], root: Union[int, None] = None) -> Tuple[int]`  
木 `tree` のハッシュ値を返す。ハッシュ値は、木の中心の数と同じサイズのタプルとなる。`root` を指定すると根付き木に対するハッシュとなる。計算量 $O(V \log V)$
