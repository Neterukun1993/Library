---
title: 二次元累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSum2D.py
---

## 概要
計算量 $O(hw)$ の前計算により、二次元配列に対する矩形和取得を計算量 $O(1)$ で行えるデータ構造。

## 使い方
`AccumulateSum2D(matrix: Sequence[Sequence[T])`  
二次元配列 `matrix` に対して、二次元累積和を構築する。`matrix` のサイズを $h × w$ としたとき、計算量 $O(hw)$

- `sum(hl: int, hr: int, wl: int, wr: int) -> T`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $O(1)$
