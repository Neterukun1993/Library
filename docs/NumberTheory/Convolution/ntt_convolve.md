---
title: 数論変換 (number-theoretic transform)
documentation_of: //NumberTheory/Convolution/ntt_convolve.py
---

## 使い方
`ntt_convolve(a: Sequence[int], b: Sequence[int]) -> List[int]`  
長さ $N$ の数列 $a$ と長さ $M$ の数列 $b$ について、$c_k = \sum_{i + j \equiv k} a_ib_j \bmod 998244353$ となる長さ $N + M - 1$ の数列 $c$ を返す。計算量 $O((N + M) \log (N + M))$
