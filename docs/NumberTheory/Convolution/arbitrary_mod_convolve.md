---
title: 任意 MOD 畳み込み
documentation_of: //NumberTheory/Convolution/arbitrary_mod_convolve.py
---

## 使い方
`arbitrary_mod_convolve(a: Sequence[int], b: Sequence[int], p: int) -> List[int]`  
長さ $N$ の数列 $a$ と長さ $M$ の数列 $b$ について、$c_k = \sum_{i + j \equiv k} a_ib_j \bmod p$ となる長さ $N + M - 1$ の数列 $c$ を返す。計算量 $O((N + M) \log (N + M))$
