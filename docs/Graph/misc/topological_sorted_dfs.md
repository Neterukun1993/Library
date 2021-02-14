---
title: トポロジカルソート (深さ優先探索)
documentation_of: //Graph/misc/topological_sorted_dfs.py
---

## 概要
有向グラフに対してトポロジカルソートをする。グラフが巡回するときは未定義。

## 使い方
`topological_sorted(digraph: Sequence[Sequence[int]]) -> List[int]`  
有向グラフに対してトポロジカルソートを行い、トポロジカル順の配列を返す。グラフが巡回ときのトポロジカル順は未定義。計算量 $O(V + E)$
