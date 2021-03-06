---
title: 一次合同方程式
documentation_of: //NumberTheory/ModularArithmetic/linear_congruence.py
---

## 概要
一次合同方程式 $ax \equiv b \pmod{m}$ を解くアルゴリズム。

## 使い方
`linear_congruence(a: int, b: int, m: int) -> Tuple[bool, int, int]`  
一次合同方程式 $ax \equiv b \pmod{m}$ に対して (解が存在するか, 最小の非負整数解, 解の周期) を返す。解が存在しない場合は `(False, -1, -1)` を返す。計算量 $O(\log \min(b, m))$
