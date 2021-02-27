---
title: 関節点・橋の列挙、DFS 木の構築 (Low Link)
documentation_of: //Graph/misc/LowLink.py
---

## 概要
無向グラフに対して DFS 木を構築する。関節点・橋の列挙が可能。

## 使い方
`LowLink(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(u: int, v: int) -> None`  
頂点 `u` と 頂点 `v` との間に無向辺を追加する。計算量 $O(1)$

- `build() -> None`  
Low Link のアルゴリズムによって DFS 木を構築する。計算量 $O(V + E)$

- `enumerate_articulations() -> Iterator[int]`  
関節点を返すイテレータを返す。1 要素のイテレートにかかる計算量 $O(1)$

- `enumerate_bridges() -> Iterator[Tuple[int, int]]`  
橋を返すイテレータを返す。1 要素のイテレートにかかる計算量 $O(1)$
