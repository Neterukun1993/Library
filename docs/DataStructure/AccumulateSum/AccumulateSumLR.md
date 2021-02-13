---
title: 左右からの累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSumLR.py
---
## 使い方
`AccumulateSumLR(array: List[Any], op: Callable[[Any, Any], Any], e: Any)`  
`array` に対して、左からの累積と右からの累積を構築する。累積は二項演算 `op`、単位元 `e` によって演算される。計算量 $O(n)$

- `left_fold(upper: int) -> Any`  
`[0, upper)` 番目の要素の累積を返す。計算量 $O(1)$

- `right_fold(lower: int) -> Any`  
`[lower, n)` 番目の要素の累積を返す。計算量 $O(1)$

- `fold(ex_idx: int) -> Any`  
`ex_idx` 番目を除いたすべての要素の累積を返す。計算量 $O(1)$
