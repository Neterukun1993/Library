---
title: いもす法 (等差数列加算)
documentation_of: //DataStructure/AccumulateSum/ImosArithmeticSequence.py
---

## 使い方
`ImosImosArithmeticSequence(n: int)`  
大きさ $n$ のいもす法用の配列を初期構築する。計算量 $O(n)$  
その後の一連の処理としては

1. `add` 関数で等差数列加算の準備をする。
2. `build` 関数で等差数列加算を実行する。
3. `__getitem__` 関数で値を取得する。

となる。

- `add(l: int, r: int, a: int, d: int) -> None`  
区間 $[l, r)$ に対して $a, a + d, a + 2 * d, \dots , a + d * (r - l + 1)$ を足す準備をする。計算量 $O(1)$

- `build() -> None`  
`add` による等差数列加算を実行する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(1)$
