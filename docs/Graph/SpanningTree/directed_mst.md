---
title: 最小有向全域木
documentation_of: //Graph/SpanningTree/directed_mst.py
---

## 概要
最小有向全域木とその総コストを求める。

## 使い方
`directed_mst(n: int, edges: Sequence[Tuple[int, int, int]], root: int)　-> Tuple[int, List[int]]`  
重み付き有向辺のリスト `edges` に対して、`root` を根とした最小有向全域木の総コスト、その有向木を表す親頂点の配列を返す。計算量 $O(E\log V)$
