---
title: KMP法 (Knuth-Morrison-Prattのアルゴリズム)
documentation_of: //String/KMP.py
---

## 使い方
`KMP(pattern: Sequence[Any])`  
検索する文字列パターン `pattern` に対して前計算する。`n = len(pattern)` としたとき、計算量 $O(n)$

- `match(text: Sequence[Any]) -> List[int]`  
全文 `text` に対して、`pattern` と一致する `text` 中のインデックスの配列を返す。`m = len(text)` としたとき、計算量 $O(m + n)$
