---
title: グリッド上のBFS
documentation_of: //Graph/ShortestPath/grid_bfs.py
---

## 概要
二次元グリッドグラフ上の単一始点最短経路問題を解くアルゴリズム。

## 使い方
`bfs(grid: Sequence[str], si: int, sj: int, wall: str) -> List[List[int]]`  
グリッドグラフ `grid` 上での、`(si, sj)` を始点とした単一始点最短距離の配列を返す。グリッドグラフの大きさを `h * w` としたとき、計算量 $O(hw)$
