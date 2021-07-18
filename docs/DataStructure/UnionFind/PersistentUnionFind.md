---
title: 永続 Union Find
documentation_of: //DataStructure/UnionFind/PersistentUnionFind.py
---

## 概要
永続化された素集合データ構造。つまり、`merge` 前後のバージョンを常に保持し、全バージョンに対する `same`、`size` が可能である。

## 使い方
`PersistentUnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n \log n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。算量 $O(\log n)$

- `merge(x: int, y: int) -> PersistentUnionFind`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合したときの `PersistentUnionFind` を返す。計算量 $O(\log n)$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $O(\log n)$

- `size(x: int) -> int`  
集合の個数を返す。計算量 $O(\log n)$
