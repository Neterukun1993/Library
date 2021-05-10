---
title: 二重辺連結成分分解
documentation_of: //Graph/Decomposition/TwoEdgeConnectedComponents.py
---

## 概要
無向グラフを二重辺連結成分分解するアルゴリズム。

## 使い方
`TwoEdgeConnectedComponents(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(u: int, v: int) -> None`  
頂点 `u` と頂点 `v` との間に無向辺を追加する。計算量 $O(1)$

- `build() -> None`  
二重辺連結成分分解を行う。`build` の実行後には、インスタンス変数である `labels` に各頂点の二重辺連結成分の番号が格納される。計算量 $O(V + E)$

- `groups() -> List[List[int]]`  
二重辺連結成分ごとに元の頂点を列挙する。計算量 $O(V)$
