---
title: 最長増加部分列 (longest increasing subsequence)
documentation_of: //DP/lis.py
---

## 概要
最長増加部分列を求めるアルゴリズム。

## 使い方
`lis(array: Sequence[int], strict: bool = True) -> List[int]`  
`array` に対する最長増加部分列を返す。`strict=False` とすると、広義最長増加部分列を返す。計算量 $O(N \log N)$
