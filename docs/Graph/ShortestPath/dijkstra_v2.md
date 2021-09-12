---
title: ダイクストラ法 ($O(V^2)$)
documentation_of: //Graph/ShortestPath/dijkstra_v2.py
---

## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。

## 使い方
`dijkstra_v2(start: int, matrix: Sequence[Sequence[int]]) -> List[int]`  
隣接行列 `matrix` で表現されるグラフ上での、始点 `start` からすべての頂点への最短距離を求める。計算量 $O(V^2)$