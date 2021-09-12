---
title: ダイクストラ法 ($O((E + V)\log V)$) + 経路復元
documentation_of: //Graph/ShortestPath/dijkstra_trace.py
---

## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。経路復元が可能。

## 使い方
- `dijkstra(start: int, graph: Sequence[Iterable[Tuple[int, int]]]) -> Tuple[List[int], List[int]]`  
$G = (V, E)$ で表される重み付き有向グラフ `graph` に対して、`start` を始点とした単一始点最短距離の配列と、経路復元用の配列を返す。計算量 $O((E + V)\log V)$

- `trace_route(goal: int, parent: List[int]) -> List[int]`  
dijkstra 法で求めた経路復元用の配列 `parent` を用いて、終点 `goal` までの頂点経路を返す。経路の頂点数を $k$ とすると、計算量 $O(k)$