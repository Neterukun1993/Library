---
title: 等差数列
documentation_of: //NumberTheory/Basic/arithmetic_sequence.py
---

## 概要
等差数列に関する基本的な公式

## 使い方
`Arithmetic.get(a0: int, d: int, i: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について $a_i$ を返す。計算量 $O(1)$

`Arithmetic.general_term(i: int, ai: int, j: int, aj: int) -> Tuple[Tuple[int, int], Tuple[int, int]]`  
$a_i$ と $a_j$ を与えたときの、等差数列の初項 $a_0$ 公差 $d$ を返す。$a_0$ と $d$ はそれぞれ (分母, 分子) を表すタプルで返される。計算量 $O(1)$

`Arithmetic.sum(a0: int, d: int, r: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について、$a_0 + a_{1} + \ldots + a_{r-1}$ を返す。計算量 $O(1)$

`Arithmetic.range_sum(a0: int, d: int, l: int, r: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について、$a_l + a_{l+1} + \ldots + a_{r-1}$ を返す。計算量 $O(1)$
