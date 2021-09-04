---
title: モンモール数 (完全順列)
documentation_of: //Combination/montmort_number.py
---
## 概要
整数 $1, 2, \dots , n$ を並び替えてできる順列において、$i$ 番目 ($1 \le i \le n$) が $i$ でない順列を完全順列 (撹拌順列) という。完全順列となる通り数 $a_n$ をモンモール数という。

モンモール数は以下の漸化式で考えることができる。

$$a_n=(n-1)(a_{n-1}+a_{n-2})$$

また、一般項を計算すると以下の式となる。

$$a_n=n!\sum_{k=2}^n\frac{(-1)^k}{k!}$$

漸化式の導出と包除原理による一般項の導出は [高校数学の美しい物語](https://manabitimes.jp/math/612) が分かりやすい。具体的な数列は OEIS [A000166](https://oeis.org/A000166) を参照。

## 使い方
`montmort_number(n: int, MOD: int) -> List[int]`  
`MOD` 上での第 `n` 項までのモンモール数のリストを返す。計算量 $O(n)$

`montmort_number2(n: int, MOD: int) -> List[int]`  
`MOD` 上での第 `n` 項までのモンモール数のリストを返す。計算量 $O(n)$

## 備考
漸化式の計算のイメージ

<img src="https://Neterukun1993.github.io/Library/montmort_number.png" width="600">
