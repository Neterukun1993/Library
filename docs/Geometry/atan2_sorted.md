---
title: 偏角ソート
documentation_of: //Geometry/atan2_sorted.py
---

## 概要
点の集合を偏角の大きさ (atan2 の大きさ) によってソートする。

## 使い方
`atan2_sorted(points: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]`  
$N$ 個の点 `points` を偏角ソートした結果を返す。点は ($x$ 座標, $y$ 座標) で与える。計算量 $O(N \log N)$
