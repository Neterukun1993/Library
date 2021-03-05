---
title: 素数列挙 (区間篩)
documentation_of: //NumberTheory/Prime/segment_sieve.py
---

## 概要
区間範囲に対して素数列挙を行うアルゴリズム。区間 $[l, r)$ についての制約が

* $1 \le l  \lt r \le 10^9$
* $r − l \le 10^6$

のようなときに使用可能。

## 使い方
`segment_sieve(l: int, r: int) -> Tuple[List[int], List[int]]`  
`l` 以上 `r` 未満の整数について、素数のリストと素数かどうかの判定テーブルを返す。計算量 $O(\sqrt r + (r - l)\log\log r)$
