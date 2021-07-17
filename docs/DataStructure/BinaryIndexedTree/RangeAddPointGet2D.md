---
title: 矩形加算・一点取得
documentation_of: //DataStructure/BinaryIndexedTree/RangeAddPointGet2D.py
---

## 概要
二次元配列に対して矩形範囲加算、一点取得を計算量 $O(\log h\log w)$ で行えるデータ構造。

## 使い方
`BinaryIndexedTree(h: int, w: int)`  
大きさ $h × w$ の二次元 Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $O(hw)$

- `get(i: int, j: int) -> int`  
$i$ 行 $j$ 列目の要素を返す。計算量$O(\log h\log w)$

- `add(hl: int, hr: int, wl: int, wr: int, val: int) -> None`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素に `val` を加える。計算量 $O(\log h\log w)$
