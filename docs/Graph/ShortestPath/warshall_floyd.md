---
title: ワーシャルフロイド法
documentation_of: //Graph/ShortestPath/warshall_floyd.py
---
## 使い方
`warshall_floyd(matrix: Sequence[Sequence[int]]) -> List[List[int]]`  
隣接行列 `matrix` で表現されるグラフ上での、全点対最短距離の配列を返す。計算量 $O(V^3)$
