---
title: RSQ_RMultipleQ
documentation_of: //DataStructure/SegmentTree/RSQ_RMultipleQ.py
---

## 概要
列に対する区間乗算、区間和取得を $O(\log n)$ で行えるデータ構造。

## 使い方
`RSQ_RMultipleQ(n: int)`  
区間乗算、区間和取得が可能な長さ $n$ の配列を構築する。配列の初期値は $0$ である。計算量 $O(n)$

- `build(array: List[int]) -> None`  
配列を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を $998244353$ で割ったあまり返す。計算量 $O(\log n)$

- `__setitem__(i: int, x: int) -> None`  
$i$ 番目の要素を `x` に更新する。計算量 $O(\log n)$

- `fold(l: int, r: int) -> int`  
$[l, r)$ 番目の区間和を $998244353$ で割ったあまりを返す。計算量 $O(\log n)$

- `apply(i: int, a: int) -> None`  
$i$ 番目の要素を `a` 倍する。計算量 $O(\log n)$

- `range_apply(l: int, r: int, a: int) -> None`  
$[l, r)$ 番目の要素をそれぞれ `a` 倍する。計算量 $O(\log n)$
