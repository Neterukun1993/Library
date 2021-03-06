---
title: 最大公約数と最小公倍数
documentation_of: //NumberTheory/Basic/gcd_lcm.py
---

## 概要
最大公約数 (greatest common divisor, GCD) と最小公倍数 (east common multiple, lcm) を求めるアルゴリズム。

## 使い方
`gcd(a: int, b: int) -> int`  
`a` と `b` の最大公約数を返す。計算量 $O(\log \min(a, b))$

`lcm(a: int, b: int) -> int`  
`a` と `b` の最小公倍数を返す。計算量 $O(\log \min(a, b))$

`all_gcd(array: Iterable[int]) -> int`  
`array` の全要素の最小公約数を返す。`n = len(array)`、`a = min(array)` とすると、計算量 $O(n + \log a)$

`all_lcm_int(array: Iterable[int]) -> int`  
`array` の全要素の最大公倍数を返す。`n = len(array)`、`a = array[0] * array[1] * ... * array[n - 1]` とすると、計算量 $O(n + \log a)$

`all_lcm_dict(array: Iterable[int]) -> Dict[int, int]`  
`array` 全要素の最大公倍数を (key, value) = (素因数, 素因数の個数) とした辞書で返す。`n = len(array)`、`a = max(array)` とすると、計算量 $O(n\sqrt a)$
