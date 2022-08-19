---
title: 巻き戻し可能 Union Find
documentation_of: //DataStructure/UnionFind/UnionFindUndo.py
---

## 概要
素集合を管理するデータ構造。集合の併合操作を巻き戻すことができる。

## 使い方
`UnionFindUndo(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $O(\log n)$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。併合に成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $O(\log n)$

- `undo() -> None`  
直前に実行した `merge` 操作を $1$ 回分巻き戻す。計算量 $O(1)$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $O(\log n)$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $O(\log n)$
