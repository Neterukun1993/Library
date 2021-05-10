---
title: 最近点対
documentation_of: //Geometry/closest_pair.py
---

## 概要
点の集合のうち最も近い点同士 (最近点対) の距離を求める分割統治アルゴリズム。

## 使い方
`closest_pair(points: Sequence[Tuple[float, float]]) -> float`  
2次元平面上の $N$ 個の点集合 `points` のうち最も近い点同士 (最近点対) の距離を返す。計算量 $O(N\log N)$
