---
title: オイラーツアー (パスに対するクエリ)
documentation_of: //Graph/Tree/EulerTourPathQuery.py
---

## 概要
オイラーツアーを行い、パスに対する一点加算、区間和取得を行うアルゴリズム。

## 使い方
`EulerTourPathQuery(tree: Sequence[Iterable[int]])`  
隣接リストで表現される木 `tree` に対してオイラーツアーを行う。同時に一点加算、区間和取得用の Binary Indexed Tree を初期構築する。計算量 $O(V\log V)$

- `lca(u: int, v: int) -> int`  
頂点 `u` と頂点 `v` の最小共通祖先を返す。計算量 $O(1)$

- `distance(u: int, v: int) -> int`  
パス `u - v` の距離を返す。計算量 $O(1)$

- `build(vals: Sequence[int]) -> None`  
頂点 `v` に対する値 `vals[v]` を格納した配列について Binary Indexed Tree を初期構築する。

- `add(u: int, val: int) -> int`  
頂点 `u` に値 `val` を加算する。計算量 $O(\log V)$

- `vertex_path_sum(u: int, v: int) -> int`  
パス `u - v` 上の頂点の値の総和を返す。計算量 $O(V\log V)$

- `edge_path_sum(u: int, v: int) -> int`  
パス `u - v` 上の辺の値の総和を返す。計算量 $O(V\log V)$`
