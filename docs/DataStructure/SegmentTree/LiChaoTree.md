---
title: Li-Chao Tree
documentation_of: //DataStructure/SegmentTree/LiChaoTree.py
---
## 使い方
`LiChaoTree(xs: Iterable[int], INF=10**18)`  
`xs` の要素を `min` クエリにおける $x$ 座標として使用可能な、空の直線 (線分) 集合を構築する。計算量 $O(n \log n)$

- `add_line(line: Tuple[int, int]) -> None`  
集合に (傾き, 切片) で表される直線 `line` を追加する。計算量 $O(\log n)$

- `add_seg(line: Tuple[int, int], l: int, r: int) -> None`  
集合に (傾き, 切片) で表される線分 `line` (ただし $x \in [l,r)$) を追加する。計算量 $O(\log ^2 n)$

- `min(x: int) -> int`  
$x$ 座標が `x` のときの、$y$ 座標の最小値を返す。そのような $y$ 座標が存在しない場合は `INF` を返す。`x` が `xs` の要素でない場合は例外 `KeyError` が発生するので注意。計算量 $O(\log n)$
