---
title: 01-BFS
documentation_of: //Graph/ShortestPath/bfs01.py
---

## 概要
各辺の長さが $0$ または $1$ の有向グラフ上で、単一始点最短経路問題を解くアルゴリズム。

## 使い方
`bfs(graph: Sequence[Sequence[Tuple[int, int]]], start: int) -> List[int]`  
重み付き有向グラフ `graph` 上での、 `start` を始点とした単一始点最短距離の配列を返す。ただし、重みは $0$ または $1$ のどちらかでなければならないことに注意。計算量 $O(V + E)$

## 参考
・[01-BFSのちょっと丁寧な解説 - ARMERIA](https://betrue12.hateblo.jp/entry/2018/12/08/000020)
