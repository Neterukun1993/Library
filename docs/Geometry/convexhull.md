---
title: 凸包
documentation_of: //Geometry/convexhull.py
---

## 概要
点集合に対する凸包を求めるアルゴリズム。

## 使い方
`convexhull(points: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]`  
2次元平面上の $N$ 個の点集合 `points` に対する凸包を返す。凸包の頂点で最も左にあるものの中で、最も下にある頂点から順に、反時計回りで返す。計算量 $O(N\log N)$
