---
title: 連立一次方程式
documentation_of: //NumberTheory/ModularArithmetic/linear_equations.py
---

## 概要
連立一次方程式 $Ax \equiv b \pmod{998244353}$ を解く。

## 使い方
`linear_equations(matrix: Sequence[Sequence[int]], vector: Sequence[int]) -> List[int, List[int], List[List[int]]]`  
$N \times M$ の係数行列 $A$ (`matrix`) と $N$ 次元ベクトル $b$ (`vector`) を与えたとき、$Ax \equiv b \pmod{998244353}$ を満たす $M$ 次元ベクトル $x$ (`result`) を返す。
$x$ が存在しない場合は `dimension` は `-1` を返す。$x$ が一意に定まる場合は `dimension` は `0` を返す。$x$ が無数に存在する場合は `dimension` は 1 以上を返す。
