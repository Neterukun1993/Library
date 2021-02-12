---
title: MP法 (Morrison-Prattのアルゴリズム)
documentation_of: //String/MP.py
---
## 使い方
`MP(s: Sequence[Any]) -> Tuple(List[int], List[int])`  
`s[:i]` の最長の境界 (Longest Border) と最短の周期 (Shortest Period) の配列を返す。`n = len(s) + 1` とすると、計算量 $O(n)$
