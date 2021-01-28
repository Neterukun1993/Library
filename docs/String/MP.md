---
title: MP法 (Morrison-Prattのアルゴリズム)
documentation_of: //String/MP.py
---
## 使い方
`MP(s: Sequence[Any]) -> List[int]`  
`s[:i]` の最長の境界 (Longest Border) を格納した長さ `n = len(s) + 1` の配列を返す。計算量 $O(n)$
