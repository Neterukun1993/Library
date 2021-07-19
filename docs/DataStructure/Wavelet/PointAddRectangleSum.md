---
title: 一点加算・矩形和取得
documentation_of: //DataStructure/Wavelet/PointAddRectangleSum.py
---

## 概要
二次元平面上の $n$ 個の重み付き点に対して、前計算を $O(n \log n)$ で行い、一点重み加算クエリに $O(\log^2n)$、矩形範囲内の重み総和クエリに $O(\log^2n)$ で答えるデータ構造。内部では Binary Index Tree を保持した Wavelet Matrix を構築する。

## 使い方
`CompressedRectangleSum(points: Iterable[Tuple[int, int, int]])`  
二次元平面上の $n$ 個の重み付き点 `points` から Wavelet Matrix を構築する。各点は ($x$ 座標, $y$ 座標, 重み) で与えられる。計算量 $O(n \log n)$

- `rect_sum(l: int, r: int, lower: int, upper: int) -> int`  
矩形範囲 $\lbrack l, r) × \lbrack lower, upper)$ に含まれる点の重みの総和を返す。計算量 $O(\log^2n)$

- `point_add(x: int, y: int, val: int) -> int`  
座標 $(x, y)$ 上の点に対して、重みを `val` 追加する。このときの点は、予め構築の際に `points` の $1$ つとして与えておく必要がある。計算量 $O(\log^2n)$
