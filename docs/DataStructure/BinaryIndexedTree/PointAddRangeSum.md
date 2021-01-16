---
title: 一点加算・区間和取得
documentation_of: //DataStructure/BinaryIndexedTree/PointAddRangeSum.py
---
## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $\mathrm{O}(n)$
- `build(array: List[Any]) -> None`  
Binary Indexed Tree を `array` で初期化する。計算量 $\mathrm{O}(n)$
- `add(i: int, val: Any) -> None`  
$i$ 番目の要素に `val` を加える。計算量 $\mathrm{O}(\log n)$
- `sum(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $\mathrm{O}(\log n)$
- `bisect_left(val: Any) -> int`  
$\lbrack 0, r)$ 番目の要素の総和が `val` 以上となる最小の $r$ を返す。そのような $r$ が存在しない場合は $n + 1$ を返す。計算量 $\mathrm{O}(\log n)$
