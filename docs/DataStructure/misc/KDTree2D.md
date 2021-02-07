---
title: 二次元領域探索 (kD-Tree)
documentation_of: //DataStructure/misc/KDTree2D.py
---
## 概要
kD-Tree: 二次元平面上の点集合から領域探索を行うデータ構造

## 使い方
`KDTree2D(points: Iterable[Tuple[int, int]])`  
二次元平面上の `n` 個の点の集合 `points` に対し、kD-Tree を構築する。計算量 $O(n \log^2 n)$

- `find(xl: int, xr: int, yl: int, yr: int) -> List[Tuple[int, int]]`  
矩形範囲 $\lbrack xl, xr) × \lbrack yl, yr)$ に含まれている点を列挙する。矩形内に含まれる点の数を `k` とすると、計算量 $O(\sqrt n + k)$
