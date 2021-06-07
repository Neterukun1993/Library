---
title: 行列累乗
documentation_of: //NumberTheory/misc/matrix_pow.py
---

## 概要
行列の累乗を求めるアルゴリズム。

## 使い方
`matrix_pow(A: Sequence[Sequence[int]], k: int, MOD: int) -> List[List[int]]`  
$n$ 次正方行列 $A$ について $A^k$ を返す。行列の各要素は $\mathrm{MOD}$ で割った余りをとる。計算量 $O(n^3 \log k)$

`matvec_mul(A: Sequence[Sequence[int]], vec: Sequence[int], MOD: int) -> List[int]`  
サイズ $n \times m$ の行列 $A$ と $m$ 次元のベクトル $v$ (`vec`) について $Av$ を返す。計算量 $O(nm)$
