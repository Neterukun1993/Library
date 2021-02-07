---
title: 動的中央値クエリ
documentation_of: //DataStructure/misc/DynamicMedian.py
---
## 概要
DynamicMedian: 集合の中央値を動的に管理するデータ構造

## 使い方
`DynamicMedian()`  
中央値を管理する空の集合を構築する。計算量 $O(1)$

- `add(val: int) -> None`  
集合に要素 `val` を追加する。集合の大きさを `n` とすると、計算量 $O(\log n)$

- `median_low() -> int`  
集合の中央値を返す。ただし、集合の大きさが偶数の場合は中央の2値の小さい方を返す。計算量 $O(1)$

- `median_low() -> int`  
集合の中央値を返す。ただし、集合の大きさが偶数の場合は中央の2値の大きい方を返す。計算量 $O(1)$

- `minimum_query() -> int`  
集合を $\{a_1, a_2, \dots, a_n \}$ としたときの $\min(|x - a_1| + |x - a_2| + ⋯ + |x - a_n|)$ を返す。$x$ は集合の中央値となる。計算量 $O(1)$
