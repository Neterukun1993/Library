---
title: Union Find
documentation_of: //DataStructure/UnionFind/UnionFind.py
---

## 概要
素集合を管理するデータ構造。

## 使い方
`UnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。併合に成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `count() -> int`  
集合の個数を返す。計算量 $O(1))$

- `groups() -> List[List[int]]`  
すべての集合とその要素を列挙する。計算量 $O(n)$
