---
title: Disjoint Sparse Table
documentation_of: //DataStructure/misc/DisjointSparseTable.py
---

## 概要
構築を $O(n\log n)$、区間畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群を要請する。

## 使い方
`DisjointSparseTable(array: Sequence[Any], op: Callable[[Any, Any], Any])`  
`array` を初期値とした Disjoint Sparse Table を構築する。`op` は畳み込み計算で用いる二項演算子である。計算量 $O(n\log n)$

- `fold(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

## 参考
[Disjoint Sparse Table と セグ木に関するポエム](https://noshi91.hatenablog.com/entry/2018/05/08/183946)
