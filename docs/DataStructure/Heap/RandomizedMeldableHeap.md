---
title: 併合可能ヒープ (Randomized Meldable Heap)
documentation_of: //DataStructure/Heap/RandomizedMeldableHeap.py
---
## 概要
ヒープ同士を計算量 $O(\log N)$ で併合可能なヒープ。

## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $O(1)$
- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$
- `push(val: int) -> None`  
ヒープに `val` を追加する。計算量 $\mathrm{expected}\ O(\log N)$
- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $\mathrm{expected}\ O(\log N)$
- `meld(other: RandomizedMeldableHeap) -> None`  
ヒープに `other` を併合する。計算量 $\mathrm{expected}\ O(\log N)$
- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $O(1)$
