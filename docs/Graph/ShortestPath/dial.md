---
title: Dial’s Algorithm
documentation_of: //Graph/ShortestPath/dial.py
---

## 概要
重み付き有向グラフ上で、単一始点最短経路問題を解くアルゴリズム。辺の重みの最大値が小さいときに、高速に動作する。

## 使い方
`dial(graph: Sequence[Sequence[Tuple[int, int]]], start: int, max_w: int) -> List[int]`  
重み付き有向グラフ `graph` 上での、 `start` を始点とした単一始点最短距離の配列を返す。辺の重みの最大値 $W$ を `max_w` として与えておく。計算量 $O(WV + E)$