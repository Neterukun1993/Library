---
title: 確率的素数判定 (ミラー・ラビン素数判定法)
documentation_of: //NumberTheory/Prime/miller_rabin.py
---

## 概要
確率的素数判定を行うアルゴリズム。$n < 2^{64}$ の範囲では決定的に素数判定できるよう実装している。

#### ミラー・ラビン素数判定法の定理
奇素数 $p = 2^s \cdot d + 1$ ($d$ は奇数) に対して、以下のいずれかが任意の整数 $a$ ($0 \lt a \lt p$) について成り立つ。

* $a^d \equiv 1 \pmod{p}$
* $a^{2^r \cdot d} \equiv -1 \pmod{p}$ となる $r$ ($0 \le r \lt s$) が存在


#### ミラー・ラビン素数判定法の定理の対偶
奇数 $n = 2^s \cdot d + 1$ ($d$ は奇数) に対して、以下のすべて満たす整数 $a$ が存在するならば、$n$ は合成数である。

* $a^d \not\equiv 1 \pmod{p}$
* 任意の $r$ ($0 \le r \lt s$)
 について $a^{2^r \cdot d} \not\equiv -1 \pmod{p}$

ミラー・ラビン素数判定法では、この対偶を用いて確率的素数判定を行う。小さい整数の範囲では決定的に素数判定できる。例えば、$a = 2, 325, 9375, 28178, 450775, 9780504, 1795265022$ を用いることで、$n < 2^{64}$ の範囲では決定的になる ([http://miller-rabin.appspot.com](http://miller-rabin.appspot.com))。

## 使い方
`miller_rabin(n: int) -> bool`  
`n` の確率的素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。`n` が $2^{64}$ までの範囲では決定的である。計算量 $O(\log n)$
