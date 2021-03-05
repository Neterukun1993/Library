---
title: 素数判定 (試し割り法)
documentation_of: //NumberTheory/Prime/is_prime.py
---

## 概要
$O(\sqrt n)$ で素数判定を行うアルゴリズム。

## 使い方
`is_prime(x: int) -> bool`  
`x` の素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。計算量 $O(\sqrt n)$
