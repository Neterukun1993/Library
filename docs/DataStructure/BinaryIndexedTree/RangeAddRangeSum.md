---
title: 区間加算・区間和取得
documentation_of: //DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
---
## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $\mathrm{O}(n)$
- `add(l: int, r: int, val: Any) -> None`  
$\lbrack l, r)$ 番目の要素それぞれに `val` を加える。計算量 $\mathrm{O}(\log n)$
- `sum(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $\mathrm{O}(\log n)$
