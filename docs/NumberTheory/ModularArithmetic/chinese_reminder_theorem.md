---
title: 中国剰余定理
documentation_of: //NumberTheory/ModularArithmetic/chinese_remainder_theorem.py
---

## 概要
$m_0, m_1, \cdots, m_{n - 1}$ と $a_0, a_1, \cdots, a_{n - 1}$ について

$$\left\{\begin{array}{l}x \equiv a_0 \pmod{m_0}\\x \equiv a_1 \pmod{m_1}\\ \cdots \\x \equiv a_{n - 1} \pmod{m_{n - 1}}\end{array}\right.$$

を満たす $x$ を求めるアルゴリズム。

## 使い方
`chinese_remainder_theorem(a: Sequence[int], m: Sequence[int]) -> Tuple[int, int]`  
$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす $x (0 \le x \lt \mathrm{lcm}(m[i]))$ とその周期 $\mathrm{lcm}(m[i])$ を返す。そのような $x$ が存在しない場合は $(-1, -1)$ を返す。計算量 $O(n \log \mathrm{lcm}(m[i]))$
