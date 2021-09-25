---
title: 最小共通祖先 (Tarjan のオフラインアルゴリズム)
documentation_of: //Graph/Tree/offline_lca.py
---

## 概要
最小共通先祖クエリにオフラインで答えるアルゴリズム。

## 使い方
`offline_lca(tree: Sequence[Iterable[int]], queries: Sequence[Tuple[int, int]], root: int) -> List[int]`  
根が `root` である木 `tree` に対して LCA を求める。計算量 $O(V + Q)$

$i$ 番目のクエリ `queries[i]` の意味は次の通りである。
```
u v
```
頂点 $u$ と頂点 $v$ の LCA は何か？

## 参考
- [Lowest Common Ancestor - Tarjan's off-line algorithm - Competitive Programming Algorithms](https://cp-algorithms.com/graph/lca_tarjan.html)