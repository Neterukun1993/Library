---
title: オイラーツアー
documentation_of: //Graph/Tree/EulerTour.py
---

## 概要
木に対してオイラーツアーを行うアルゴリズム。森にも対応している。

## 使い方
`EulerTour(tree: Sequence[Iterable[int]], root: Optional[int] = None)`  
隣接リストで表現される木 `tree` に対してオイラーツアーを行う。根頂点 `root` を指定しない場合は、頂点 `0` が根となる。計算量 $O(V)$

- `build_lca() -> None`  
最小共通祖先クエリを答えるための前計算 (ダブリング) を行う。計算量 $O(V\log V)$

- `lca(u: int, v: int) -> int`  
`u` と `v` の最小共通祖先を返す。`u` と `v` が非連結の場合は `-1` を返す。計算量 $O(1)$
