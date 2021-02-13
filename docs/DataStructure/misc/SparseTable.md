---
title: Sparse Table
documentation_of: //DataStructure/misc/SparseTable.py
---

## 概要
構築を $O(n\log n)$、区間畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群 + 冪等性を要請する。

## 使い方
`SparseTable(array: Sequence[Any], op: Callable[[Any, Any], Any])`  
`array` を初期値とした Sparse Table を構築する。`op` は畳み込み計算で用いる二項演算子である。計算量 $O(n\log n)$

- `fold(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$
