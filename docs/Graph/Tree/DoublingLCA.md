---
title: 最小共通祖先 (ダブリング)
documentation_of: //Graph/Tree/DoublingLCA.py
---

## 概要
木に対して $O(V \log V)$ で構築し、$O(\log V)$ で最小共通先祖クエリに答えるアルゴリズム。森にも対応している。

## 使い方
`DoublingLCA(tree: Sequence[Iterable[int]], root: Optional[int] = None)`  
隣接リストで表現される木 `tree` に対してダブリングを行う。根頂点 `root` を指定しない場合は、頂点 `0` が根となる。計算量 $O(V\log V)$

- `lca(u: int, v: int) -> int`  
`u` と `v` の最小共通祖先を返す。`u` と `v` が非連結の場合は `-1` を返す。計算量 $O(\log V)$

- `distance(u: int, v: int) -> int`  
`u` - `v` パスの距離を返す。`u` と `v` が非連結の場合は `-1` を返す。計算量 $O(\log V)$

- `jump(u: int, v: int, k: int) -> int`  
`u` - `v` パス上の頂点で `u` からの距離が `k` の頂点を返す。そのような頂点が存在しない場合は `-1`を返す。計算量 $O(\log V)$
