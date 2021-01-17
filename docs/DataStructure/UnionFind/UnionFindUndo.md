---
title: 巻き戻し可能Union Find
documentation_of: //DataStructure/UnionFind/UnionFindUndo.py
---
## 使い方
`UnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、 $n$ 個の素集合を構築する。計算量 $\mathrm{O}(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{O}(\log n)$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{O}(\log n)$

- `undo() -> None`  
直前に実行した `merge` 操作を1回分巻き戻す。計算量 $\mathrm{O}(1)$

- `same(x: int, y: int) -> bool`  
要素 $x, y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{O}(\log n)$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{O}(\log n)$
