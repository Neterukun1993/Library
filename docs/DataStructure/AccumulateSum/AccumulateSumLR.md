---
title: 左右からの累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSumLR.py
---

## 概要
計算量 $O(n)$ の前計算により、列に対する区間取得を計算量 $O(1)$ で行えるデータ構造。

通常の累積和の場合には、演算に関する逆元が必要であるが、この累積和には逆元が不要（二項演算と単位元をもつモノイドで十分）である。その代わりに、左端からの累積もしくは右端からの累積しか取ることができない。[ABC125-C GCD on Blackboard](https://atcoder.jp/contests/abc125/tasks/abc125_c) のような問題で役立つ。

## 使い方
`AccumulateSumLR(array: Sequence[T], op: Callable[[T, T], T], e: T)`  
長さ $n$ の配列 `array` に対して、左からの累積と右からの累積を構築する。累積は二項演算 `op`、単位元 `e` によって演算される。計算量 $O(n)$

- `left_fold(upper: int) -> T`  
`[0, upper)` 番目の要素の累積を返す。計算量 $O(1)$

- `right_fold(lower: int) -> T`  
`[lower, n)` 番目の要素の累積を返す。計算量 $O(1)$
