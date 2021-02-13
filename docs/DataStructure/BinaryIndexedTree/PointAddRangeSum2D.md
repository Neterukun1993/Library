---
title: 一点加算・矩形和取得
documentation_of: //DataStructure/BinaryIndexedTree/PointAddRangeSum2D.py
---

## 使い方
`BinaryIndexedTree(h: int, w: int)`  
大きさが $h × w$ の二次元 Binary Indexed Tree を構築する。初期値はすべて `0` である。計算量 $O(hw)$

- `add(i: int, j: int, val: int) -> None`  
`i` 番目の行、`j` 番目の列の要素に `val` を加える。計算量 $O(\log h\log w)$

- `sum(hl: int, hr: int, wl: int, wr: int) -> int`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $O(\log h\log w)$
