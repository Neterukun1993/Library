---
title: 強連結成分分解 (Kosarajuのアルゴリズム)
documentation_of: //Graph/Decomposition/SCC_Kosaraju.py
---

## 概要
有向グラフを強連結成分分解するアルゴリズム。

## 使い方
`StronglyConnectedComponents(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(v: int, nxt_v: int) -> None`  
頂点 `v` から頂点 `nxt_v` への有向辺を追加する。計算量 $O(1)$

- `build() -> None`  
強連結成分分解を行う。`build` の実行後には、インスタンス変数である `labels` に各頂点の強連結成分の番号 (縮約後の頂点番号) が格納される。縮約後の頂点番号はトポロジカルソート順である。計算量 $O(V + E)$

- `construct_dag() -> Tuple[List[List[int]], List[int]]`  
縮約後の頂点による有向グラフと、縮約後の頂点が含む元の頂点を返す。計算量 $O(V + E)$
