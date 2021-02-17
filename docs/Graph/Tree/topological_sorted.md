---
title: 木上のトポロジカルソート
documentation_of: //Graph/Tree/topological_sorted.py
---

## 概要
木 (もしくは森) に対してトポロジカルソートをする。木 DP を非再帰で行いたいときに使用する。

## 使い方
`topological_sorted(tree: Sequence[Iterable[int]], root: Optional[int] = None) -> Tuple[List[int], List[int]]`  
木（もしくは森）に対してトポロジカルソートを行い、トポロジカル順の配列と親頂点の配列を返す。根頂点 `root` を指定しない場合は、未訪問の頂点すべてに対してトポロジカルソートを行う。計算量 $O(V)$
