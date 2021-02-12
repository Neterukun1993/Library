---
title: 辺情報を頂点情報へと変換
documentation_of: //Graph/misc/edge_to_vertex.py
---
## 使い方
`edge_to_vertex(n: int, edges: List) -> Tuple[List, List]`
重み付きの辺 `edges` をもつ `n` 頂点のグラフに対して、辺情報を頂点情報に変換した結果を返す。計算量 $O(V + E)$

## 備考
以下の図の通り。
<img src="https://Neterukun1993.github.io/Library/edge_to_vertex.png" width="600">
