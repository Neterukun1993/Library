---
title: ラグランジュ補間
documentation_of: //NumberTheory/ModularArithmetic/lagrange_interpolation.py
---

## 概要
$x$ が相異なる $n + 1$ 個の点 $(x_0, y_0),\ldots,(x_n, y_n)$ 全てに対して $f(x_i) = y_i$ を満たす $n$ 次多項式 $f$ を考える。このときに $f(T)$ の値を求めるアルゴリズム。

## 使い方
`lagrange_interpolation_naive(points: Iterable[[int, int]], T: int, MOD: int) -> int`  
$N + 1$ 個の点 `points` を通る $N$ 次多項式 $f$ について、$f(T)$ の値を返す。計算量 $O(N^2)$

`lagrange_interpolation(y: Sequence[int], T: int, MOD: int) -> int`  
$N$ 次多項式 $f$ について $f(0), f(1), \ldots, f(N)$ の値を配列 `y` として与えたとき 、$f(T)$ の値を返す。計算量 $O(N + \log\mathrm{MOD})$

## Verify
問題: [ARC003-D 見たことのない多項式](https://atcoder.jp/contests/arc033/tasks/arc033_4)  
提出: https://atcoder.jp/contests/arc033/submissions/28588350