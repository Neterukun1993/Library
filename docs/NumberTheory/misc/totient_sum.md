---
title: オイラーの $\varphi$ 関数の和
documentation_of: //NumberTheory/misc/totient_sum.py
---

## 使い方
`totient_sum(n: int, MOD: int) -> int`  
$\sum_{i=1}^{n}{\varphi(i)}$ を $\mathrm{MOD}$ で割ったあまりを返す。計算量 $O(N^{2/3}(\log\log{N})^{1/3})$

## 参考
[トーティエント関数 $\varphi(i)$ の和 $\sum_{i=1}^{N}{\varphi(i)}$ を $O(N^{2/3}(\log\log{N})^{1/3})$ で求める Wiki - yukicoder](https://yukicoder.me/wiki/sum_totient)