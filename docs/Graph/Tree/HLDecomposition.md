---
title: HL分解 (Heavy-Light Decomposition)
documentation_of: //Graph/Tree/HLDecomposition.py
---

## 概要
木に対して HL 分解 (Heavy-Light Decomposition) を行い、列としてのクエリ処理を可能にするアルゴリズム。

## 使い方
`HLDecomposition(tree: Sequence[Iterable[int]])`  
隣接リストで表現される木 `Tree` に対して HL 分解を行う。森にも対応している。**根頂点を指定できないことに注意。木の場合、根は頂点 `0` となる。** 計算量 $O(V)$

- `__getitem__(v: int) -> int`  
木の頂点 `v` に対応する列のインデックスを返す。計算量 $O(1)$

- `lca(u: int, v: int) -> int`  
`u` と `v` の最小共通祖先を返す。`u` と `v` が非連結の場合は `-1` を返す。計算量 $O(\log V)$

- `distance(u: int, v: int) -> int`  
`u` - `v` パスの距離を返す。`u` と `v` が非連結の場合は `-1` を返す。計算量 $O(\log V)$

- `range_vertex_path(u: int, v: int) -> Iterator[Tuple[int, int]]`  
`u` - `v` パス上の頂点に対応する列の区間集合をイテレータとして返す。区間は半開区間である。`u` と `v` が非連結の場合は未定義。イテレートにかかる計算量 $O(\log V)$

- `range_edge_path(u: int, v: int) -> Iterator[Tuple[int, int]]`  
`u` - `v` パス上の辺に対応する列の区間集合をイテレータとして返す。区間は半開区間である。`u` と `v` が非連結の場合は未定義。イテレートにかかる計算量 $O(\log V)$

- `range_subtree(u: int) -> Tuple[int, int]`  
`u` を根とした部分木に対応する列の区間を返す。区間は半開区間である。計算量 $O(1)$

## 参考
- [【図解】木のパスに関するクエリは HL 分解！ その仕組みと実装を図で理解する｜Heavy-Light Decomposition - Qiita](https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3)
- [Easiest HLD with subtree queries - Codeforces](https://codeforces.com/blog/entry/53170)