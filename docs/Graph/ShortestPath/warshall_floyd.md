---
title: ワーシャルフロイド法
documentation_of: //Graph/ShortestPath/warshall_floyd.py
---

## 概要
重み付き有向グラフにおける全点対最短距離問題を解くアルゴリズム。各辺の重みは負でもよい。

## 使い方
`warshall_floyd(matrix: Sequence[Sequence[int]]) -> List[List[int]]`  
隣接行列 `matrix` で表現されるグラフ上での、全点対最短距離の配列を返す。計算量 $O(V^3)$

## 備考
- 頂点 $u$ が負閉路に含まれるとき、$u$ - $u$ 間の最短距離 `distance[u][u]` が負になる。
- ある辺を既存の辺より小さいコストの辺に変更するとき、$O(V^2)$ で更新ができる。[ARC035-C](https://atcoder.jp/contests/arc035/tasks/arc035_c)
