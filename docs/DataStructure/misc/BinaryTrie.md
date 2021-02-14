---
title: Binary Trie
documentation_of: //DataStructure/misc/BinaryTrie.py
---

## 概要
Trie 構造で非負整数を管理するデータ構造。

## 使い方
`BinaryTrie(MAX_BIT_LENGTH=32)`  
空の集合を構築する。集合に格納できる 2 進数での最大桁数を `MAX_BIT_LENGTH` (これを $\sigma$ とする) で指定する。計算量 $O(1)$

- `search(val: int) -> bool`  
`val` が集合に属しているか返す。計算量 $O(\sigma)$

- `insert(val: int) -> bool`  
集合に `val` を追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。計算量 $O(\sigma)$

- `delete() -> int`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\sigma)$

- `get_xor_min(xor_val: int) -> int`  
集合内の要素と `xor_val` との bitwise-xor をとった場合に考えられる最小値を返す。計算量 $O(\sigma)$
