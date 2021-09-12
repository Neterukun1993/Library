---
title: ダイクストラ法 (Radix Heap)
documentation_of: //Graph/ShortestPath/dijkstra_radix.py
---

## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。

## 使い方
`dijkstra(start: int, graph: Sequence[Iterable[Tuple[int, int]]], LIMIT: int = 1<<64) -> List[int]`  
$G = (V, E)$ で表される重み付き有向グラフ `graph` に対して、`start` を始点とした単一始点最短距離の配列を返す。計算量 $O((E + V)\log \mathrm{LIMIT})$