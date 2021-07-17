---
title: 累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSum.py
---

## 概要
計算量 $O(n)$ の前計算により、列に対する区間和取得を計算量 $O(1)$ で行えるデータ構造。

## 使い方
`AccumulateSum(array: Sequence[T])`  
大きさ $n$ の配列 `array` の累積和を構築する。計算量 $O(n)$

- `sum(l: int, r: int) -> T`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(1)$
