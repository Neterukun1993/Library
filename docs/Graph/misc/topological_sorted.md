---
title: 有向グラフ上のトポロジカルソート (Kahn のアルゴリズム)
documentation_of: //Graph/misc/topological_sorted.py
---

## 概要
有向グラフに対してトポロジカルソートをする。グラフが巡回するときは未定義。

## 使い方
`topological_sorted(digraph: Sequence[Sequence[int]], root=None) -> Tuple[bool, List[int]]`  
有向グラフに対してトポロジカルソートを行い、非巡回判定 ( `True` : 非巡回、`False` : 巡回あり) とトポロジカル順の配列を返す。判定が `False` の場合、トポロジカル順は未定義。計算量 $O(V + E)$
