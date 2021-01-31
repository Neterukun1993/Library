---
title: 01-BFS
documentation_of: //Graph/ShortestPath/bfs01.py
---
## 使い方
`bfs(graph: Sequence[Sequence[Tuple[int, int]]], start: int) -> List[int]`  
重みつきグラフ `graph` 上での、 `start` を始点とした単一始点最短距離の配列を返す。ただし、重みは `0` または `1` のどちらかでなければならないことに注意。計算量 $O(V + E)$
