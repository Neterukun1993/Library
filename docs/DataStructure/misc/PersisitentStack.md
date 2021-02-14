---
title: 永続Stack
documentation_of: //DataStructure/misc/PersistentStack.py
---

## 概要
Stack を永続化したデータ構造。一応、経路復元などに使える。

## 使い方
`PersistentStack(val=None, prev=None)`  
空の Persistent Stack を構築する。計算量 $O(1)$

- `top() -> Any`  
Persistent Stack の末尾の要素を返す。計算量 $O(1)$

- `push(val: Any) -> PersistentStack`  
末尾に要素 `val` を追加した Persistent Stack を返す。計算量 $O(1)$

- `pop() -> PersistentStack`  
末尾の要素を削除した Persistent Stack を返す。計算量 $O(1)$`
