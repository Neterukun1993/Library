---
title: 素数列挙 + 素因数分解 (線形篩)
documentation_of: //NumberTheory/linear_sieve.py
---

## 概要
$O(n)$ で素数列挙を行うアルゴリズム。副産物の最小素因数によって $O(\log n)$ で素因数分解ができる。

## 使い方
`linear_sieve(n: int) -> Tuple[List[int], List[int]]`  
整数 `n` 以下の素数のリストと、各整数について最小素因数のテーブルを返す。計算量 $O(n)$

`prime_factors(n: int, mindiv_factor: Sequence[int]) -> List[int]`  
整数 `n` を素因数分解した結果のリストを返す。線形篩によって求めた最小素因数のテーブル `mindiv_factor` を引数に取る。計算量 $O(\log n)$
