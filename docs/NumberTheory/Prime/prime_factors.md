---
title: 素因数分解 (試し割り法)
documentation_of: //NumberTheory/Prime/prime_factors.py
---

## 概要
$O(\sqrt n)$ で素因数分解を行うアルゴリズム。

## 使い方
`prime_factors(n: int) -> List[int]`  
整数 `n` を素因数分解した結果のリストを返す。計算量 $O(\sqrt n)$

`prime_factors_distinct(n, int) -> List[int]`  
整数 `n` を素因数分解し、素因数の重複を除いた結果のリストを返す。計算量 $O(\sqrt n)$

`prime_factors_compress(n, int) -> List[Tuple[int, int]]`  
整数 `n` を素因数分解し、(素因数, 素因数の個数) の組として結果のリストを返す。計算量 $O(\sqrt n)$
