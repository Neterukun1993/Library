---
title: 遅延評価 Binary Trie
documentation_of: //DataStructure/misc/LazyBinaryTrie.py
---

## 概要
Trie 構造で非負整数を管理するデータ構造。集合内の全要素に対する xor を行うことができる。

## 使い方
`LazyBinaryTrie(MAX_BIT_LENGTH=32)`  
空の集合を構築する。集合に格納できる 2 進数での最大桁数を `MAX_BIT_LENGTH` (これを $\sigma$ とする) で指定する。計算量 $O(1)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__contains__(val: int) -> bool`  
`val` が集合に属しているか返す。計算量 $O(\sigma)$

- `add(val: int) -> bool`  
集合に `val` を追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。計算量 $O(\sigma)$

- `remove(val: int) -> int`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\sigma)$

- `kth_smallest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\sigma)$

- `kth_largest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\sigma)$

- `bisect_left(lower: int) -> int`  
集合内で `lower` 以上の値が現れる最初のインデックスを返す。計算量 $O(\sigma)$

- `bisect_right(upper: int) -> int`  
集合内で `upper` よりも大きい値が現れる最初のインデックスを返す。計算量 $O(\sigma)$

- `get_xor_min(val: int) -> int`  
集合内の要素と `val` との bitwise-xor をとった場合に考えられる最小値を返す。計算量 $O(\sigma)$

- `all_xor(val: int) -> None`  
集合内の全要素に対して `val` の bitwise-xor を行う。計算量 $O(1)$ 
