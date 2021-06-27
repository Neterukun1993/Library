---
title: 永続 Queue (Banker's Queue)
documentation_of: //DataStructure/misc/BankersQueue.py
---

## 概要
Queue を永続化したデータ構造。

## 使い方
`BankersQueue()`  
空の Banker's Queue を構築する。計算量 $O(1)$

- `front() -> Any`  
Banker's Queue の先頭の要素を返す。計算量 $O(1)$

- `push(val: Any) -> BankersQueue`  
末尾に要素 `val` を追加した Banker's Queue を返す。計算量 $\mathrm{amortized} O(1)$

- `pop() -> BankersQueue`  
先頭の要素を削除した Banker's Queue を返す。計算量 $\mathrm{amortized} O(1)$

## 参考
[銀行家の Queue (37zigen さん)](https://37zigen.com/bankers-queue/)
