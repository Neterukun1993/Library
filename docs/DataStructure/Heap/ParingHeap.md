---
title: 併合可能ヒープ (Paring Heap)
documentation_of: //DataStructure/Heap/ParingHeap.py
---
## 概要
ヒープ同士を計算量 $O(\log N)$ で併合可能なヒープ。

## 使い方
`ParingHeap()`  
空のヒープを作成する。計算量 $O(1)$
- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $O(1)$
- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$
- `push(val: int) -> None`  
ヒープに `val` を追加する。計算量 $O(\log N)$
- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $O(\log N)$
- `meld(other: ParingHeap) -> None`  
ヒープに `other` を併合する。計算量 $O(\log N)$
