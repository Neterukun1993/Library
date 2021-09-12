---
title: Lucas の定理
documentation_of: //Combination/LucasTheorem.py
---
## 概要
二項係数を素数で割ったときのあまりを求める。

## 使い方
`LucasTheorem(p: int)`  
素数 $p$ 上での前計算を行う。計算量 $O(p)$

- `comb(n: int, k: int) -> int`  
${}_n\mathrm{C}_k \pmod{p}$ を返す。計算量 $O(\log k)$
