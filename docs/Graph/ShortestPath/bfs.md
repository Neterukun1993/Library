---
title: BFS
documentation_of: //Graph/ShortestPath/bfs.py
---

## 概要
各辺の長さが $1$ の有向グラフ上で、単一始点最短経路問題を解くアルゴリズム。

## 使い方
`bfs(graph: Sequence[Sequence[int]], start: int) -> List[int]`  
各辺の長さが $1$ の有向グラフ `graph` 上での、`start` を始点とした単一始点最短距離の配列を返す。計算量 $O(V + E)$
