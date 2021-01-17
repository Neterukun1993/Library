---
title: 左右からの累積和
documentation_of: //DataStructure/AccumulateSum/AccumulateSumLR.py
---
## 使い方
`AccumulateSumLR(array: List[Any], op: Callable[[Any, Any], Any], e: Any)`  
`array` の累積和を構築する。このときの累積は二項演算 `op`、単位元 `e` によって演算される。`array` のサイズを $n$ としたとき、計算量 $\mathrm{O}(n)$
- `left_fold(upper: int) -> Any`  
$\lbrack 0, upper)$ 番目の要素の累積を返す。計算量 $\mathrm{O}(1)$
- `right_fold(upper: int) -> Any`  
$\lbrack lower, n)$ 番目の要素の累積を返す。計算量 $\mathrm{O}(1)$
- `fold(ex_idx: int) -> Any`  
$ex\_idx$ 番目を除いたすべての要素の累積を返す。計算量 $\mathrm{O}(1)$
