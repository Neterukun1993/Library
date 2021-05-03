---
title: きたまさ法
documentation_of: //misc/kitamasa.py
---

## 使い方
`kitamasa(a: Sequence[int], d: Sequence[int], n: int):`  
初めの $k$ 項 $(a_0, a_1, \dots, a_{k-1})$ と係数 $d = (d_0, d_1, \dots, d_{k-1})$ による漸化式

$$a_{n} = d_0 a_{n-k} + d_1 a_{n-k + 1} + \dots + d_{k-1} a_{n-1}$$

で定まる数列の第 $n$ 項 $a_n$ を返す。$n$ は 0-indexed であることに注意。計算量 $O(K^2 \log N)$
