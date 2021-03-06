---
title: 拡張ユークリッドの互除法
documentation_of: //NumberTheory/Basic/extended_gcd.py
---

## 使い方
`extended_gcd(a: int, b: int) -> Tuple[int, int, int]`  
$\gcd(a, b)$ の結果および $ax + by = \gcd(a, b)$ の整数解 $(x, y)$ を返す。計算量 $O(\log \min(a, b))$
