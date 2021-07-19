---
title: 種類数取得
documentation_of: //DataStructure/Wavelet/RangeSetQuery.py
---

## 使い方
`RangeSetQuery(array: Sequence[int])`  
長さ $n$ の配列 `array` から Wavelet Matrix を構築する。計算量 $O(n \log n)$

- `query(l: int, r: int) -> int`  
範囲 $\lbrack l, r)$ に含まれる要素の種類数を返す。計算量 $O(\log n)$
