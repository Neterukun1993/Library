---
title: 平方剰余 (Tonelli-Shanks)
documentation_of: //NumberTheory/misc/tonelli_shanks.py
---

## 概要
整数 $a$ と素数 $p$ が与えられたとき $x^2 \equiv a \pmod{p}$ を満たす $x$ を求めるアルゴリズム。

## 使い方
`tonelli_shanks(a: int, p: int) -> int`  
$x^2 \equiv a \pmod{p}$ を満たす $x$ を返す。そのような $x$ が存在しない場合は `-1` を返す。計算量 $O(\log^2 p)$
