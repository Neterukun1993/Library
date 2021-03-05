---
title: 素数列挙 (エラトステネスの篩)
documentation_of: //NumberTheory/eratosthenes_sieve.py
---

## 概要
$O(n\log \log n)$ で素数列挙を行うアルゴリズム。

## 使い方
`eratosthenes_sieve(n: int) -> Tuple[List[int], List[int]]`  
`n` 以下の素数のリストと、素数かどうかの判定テーブルを返す。計算量 $O(n \log \log n)$
