---
title: ヒストグラム中の最大長方形
documentation_of: //DP/largest_rectangle_in_histogram.py
---

## 概要
ヒストグラム中の最大長方形の面積を求めるアルゴリズム。スタックを用いた方法により、ビンの数の線形時間で計算できる。

## 使い方
`largest_rectangle_in_histogram(heights: Sequence[int]) -> int`  
$N$ 個のビン `heights` を持つヒストグラム中の最大長方形の面積を返す。計算量 $O(N)$
