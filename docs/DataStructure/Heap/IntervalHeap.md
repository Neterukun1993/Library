---
title: Interval Heap
documentation_of: //DataStructure/Heap/IntervalHeap.py
---
## 概要
最小値と最大値を同時に管理するヒープ。

## 使い方
`IntervalHeap()`  
空のヒープを作成する。計算量 $O(1)$
- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$
- `max -> int`  
ヒープ内の最大の値を返す。計算量 $O(1)$
- `__len__() -> int`  
ヒープの大きさを返す。計算量 $O(1)$
- `push(val: int)`  
ヒープに `val` を追加する。計算量 $(\log N)$
- `pop_min() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $(\log N)$
- `pop_max() -> int`  
ヒープ内の最大の値を削除してその値を返す。計算量 $(\log N)$
