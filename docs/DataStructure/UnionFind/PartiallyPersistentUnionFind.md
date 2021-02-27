---
title: 部分永続 Union Find
documentation_of: //DataStructure/UnionFind/PartiallyPersistentUnionFind.py
---
## 使い方
`PartiallyPersistentUnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、`n` 個の素集合を構築する。計算量 $O(n)$

- `root(t: int, x: int) -> int`  
時刻 `t` における、要素 `x` の代表元を返す。計算量 $O(\log n)$

- `merge(t: int, x: int, y: int) -> bool`  
時刻 `t` において、要素 `x` を含む集合と要素 `y` を含む集合を併合する。成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $O(\log n)$

- `same(t: int, x: int, y: int) -> bool`  
時刻 `t` において、要素 `x` と 要素 `y` が同じ集合に属するかどうかを返す。計算量 $O(\log n)$

- `size(t: int, x: int) -> int`  
時刻 `t` における、要素 `x` を含む集合の大きさを返す。計算量 $O(\log n)$
