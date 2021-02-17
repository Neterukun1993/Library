---
title: 木の直径
documentation_of: //Graph/Tree/diameter.py
---

## 概要
木の直径を求めるアルゴリズム。

## 使い方
`diameter(tree: Sequence[Iterable[Tuple[int, int]]]) -> Tuple[int, List[int]]`  
隣接リストで表現された重み付き木 `tree` の直径とそのパスを返す。計算量 $O(V)$
