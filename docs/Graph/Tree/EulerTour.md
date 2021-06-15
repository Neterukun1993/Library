---
title: オイラーツアー
documentation_of: //Graph/Tree/EulerTour.py
---

## 概要
木に対してオイラーツアーを行うアルゴリズム。

## 使い方
`EulerTour(tree: Sequence[Iterable[int]], root: int)`  
根頂点が `root` である隣接リストで表現される木 `tree` に対してオイラーツアーを行う。計算量 $O(V\log V)$

- `lca(u: int, v: int) -> int`  
頂点 `u` と頂点 `v` の最小共通祖先を返す。計算量 $O(1)$

- `distance(u: int, v: int) -> int`  
パス `u - v` の距離を返す。計算量 $O(1)$
