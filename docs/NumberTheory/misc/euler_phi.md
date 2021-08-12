---
title: オイラーの $\varphi$ 関数
documentation_of: //NumberTheory/misc/euler_phi.py
---

## 使い方
`euler_phi(n: int) -> int`  
正の整数 $n$ について、$n$ と互いに素な $n$ 以下の正の整数の個数を返す。計算量 $O(\sqrt{n})$

`euler_phi_table(n: int) -> List[int]`  
$n$ 以下の $\varphi (n)$ をすべて求めたテーブルを返す。計算量 $O(n \log \log n)$
