---
title: 最小全域木 (クラスカル法)
documentation_of: //Graph/SpanningTree/kruskal.py
---

## 概要
クラスカル法により最小全域木の総コストを求める。

## 使い方
`prim(graph: Sequence[Iterable[Tuple[int, int]]]) -> int`  
隣接リストで表現される無向グラフ `graph` に対して、最小全域木の総コストを返す。計算量 $O(E\log V)$
