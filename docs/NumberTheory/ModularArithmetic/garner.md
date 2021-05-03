---
title: Garner のアルゴリズム
documentation_of: //NumberTheory/ModularArithmetic/garner.py
---

## 概要
$m_0, m_1, \cdots, m_{n - 1}$ と $a_0, a_1, \cdots, a_{n - 1}$ について

$$\left\{\begin{array}{l}x \equiv a_0 \pmod{m_0}\\x \equiv a_1 \pmod{m_1}\\ \cdots \\x \equiv a_{n - 1} \pmod{m_{n - 1}}\end{array}\right.$$

を満たす $x$ を求めるアルゴリズム。

## 使い方
`pregarner(a: Sequence[int], m: Sequence[int], MOD: int) -> Tuple[int, Sequence[int], Sequence[int]]`  
互いに素でない $m_i, m_j (i \ne j)$ があるときに Garner のアルゴリズムを適応するための前処理
を行う。
- $1$ 番目の返り値が $-1$ のとき、$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす $x$ は存在しない。このときの $2, 3$ 番目の返り値は未定義。
- $1$ 番目の返り値が $-1$ でないとき、$1$ 番目の返り値は $\mathrm{MOD}$ 上の $\mathrm{lcm}(m[i])$ である。$2, 3$ 番目の返り値は前処理された $a$ と $m$ である。

`pregarner(a: Sequence[int], m: Sequence[int], MOD: int) -> Tuple[int, Sequence[int], Sequence[int]]`  
$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす最小の非負整数 $x$ を $\mathrm{MOD}$ で割った余りを返す。そのような $x$ が存在しない場合は $-1$ を返す。計算量 $O(N^2)$
