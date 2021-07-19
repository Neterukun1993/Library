---
title: Radix Heap
documentation_of: //DataStructure/Heap/RadixHeap.py
---

## 使い方
`RadixHeap(LIMIT: int)`  
格納可能な最大値 `LIMIT` を指定した空のヒープを作成する。計算量 $O(\log \mathrm{LIMIT})$

- `__len__() -> int`  
ヒープの大きさを返す。計算量 $O(1)$

- `push(val: int) -> None`  
ヒープに `val` を追加する。ただし、最後に pop した値よりも小さな値は入れられない。計算量 $O(\log \mathrm{LIMIT})$

- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $O(\log \mathrm{LIMIT})$
