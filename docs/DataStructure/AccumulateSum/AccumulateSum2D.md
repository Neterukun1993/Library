---
title: 二次元累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSum2D.py
---

## 使い方
`AccumulateSum2D(matrix: List[List[Any])`  
`matrix` の二次元累積和を構築する。`matrix` のサイズを $h × w$ としたとき、計算量 $O(hw)$

- `sum(hl: int, hr: int, wl: int, wr: int) -> Any`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $O(1)$
