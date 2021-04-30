---
title: 約数列挙 (試し割り法)
documentation_of: //NumberTheory/Prime/divisors.py
---

## 概要
$O(\sqrt n)$ で約数列挙を行うアルゴリズム。

## 使い方
`divisors(n: int) -> List[int]`  
整数 `n` の約数を昇順列挙した結果のリストを返す。計算量 $O(\sqrt n)$
