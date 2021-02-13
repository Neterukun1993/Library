---
title: 二次元Sparse Table
documentation_of: //DataStructure/misc/SparseTable2D.py
---

## 概要
構築を $O(hw\log h\log w)$、矩形畳み込みを $O(1)$ で行える二次元データ構造。畳み込みは半群 + 冪等性を要請する。定数倍が重いので注意。

## 使い方
`SparseTable(matrix: Sequence[Sequence[Any]], op: Callable[[Any, Any], Any])`  
大きさ $h × w$ の `matrix` を初期値とした 二次元 Sparse Table を構築する。`op` は畳み込み計算で用いる二項演算子である。計算量 $O(hw\log h\log w)$

- `fold(hl: int, hr: int, wl: int, wr: int) -> Any`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の畳み込み結果を返す。計算量 $O(1)$
