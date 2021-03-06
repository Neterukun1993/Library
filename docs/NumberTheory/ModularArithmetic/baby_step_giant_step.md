---
title: 離散対数 (Baby-step giant-step)
documentation_of: //NumberTheory/ModularArithmetic/baby_step_giant_step.py
---

## 概要
整数 $x, y, m$ が与えられたとき $x^k \equiv y \pmod{m}$ を満たす $k$ を求めるアルゴリズム。

## 使い方
`baby_step_giant_step(x: int, y: int, MOD: int) -> int`  
`MOD` 上で $x^k \equiv y$ を満たす $k$ を返す。そのような $k$ が存在しない場合は `-1` を返す。計算量 $O(\sqrt {\mathrm{MOD}})$
