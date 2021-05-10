---
title: 最小全域木 (ブルーフカ法)
documentation_of: //Graph/SpanningTree/boruvka.py
---

## 概要
ブルーフカ法により最小全域木の総コストを求める。

## 使い方
`boruvka(n: int, edges: Iterable[Tuple[int, int, int]]) -> int`  
頂点数 `n` の無向グラフ $G=(V, E)$ に対して、重み付き辺集合 `edges` から構成される最小全域木の総コストを返す。計算量 $O(E\log V)$
