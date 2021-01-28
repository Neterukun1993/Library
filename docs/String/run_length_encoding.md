---
title: ランレングス圧縮
documentation_of: //String/run_length_encoding.py
---

## 使い方
`encoding(s: Sequence[Any]) -> List[Tuple[Any, int]]`  
`s` 中の連続した同じ要素をまとめて (要素, 連続した回数) のタプルに変換した結果を返す。`n = len(s)` としたとき、計算量 $O(n)$
