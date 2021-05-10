---
title: ベルマンフォード法
documentation_of: //Graph/ShortestPath/bellman_ford.py
---
## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。各辺の重みは負でもよい。

## 使い方
`bellman_ford(start: int, graph: Sequence[Iterable[Tuple[int, int]]]) -> Tuple[bool, List[int]]`  
$G = (V, E)$ で表される重み付き有向グラフ `graph` に対して、始点 `start` からすべての頂点への最短距離を求める。始点からたどり着ける負閉路が存在しないときは `True` と最短距離のリストを返す。一方で、始点からたどり着ける負閉路が存在するときは `False` と要素未定義のリストを返す。計算量 $O(VE)$
