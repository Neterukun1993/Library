---
title: 併合可能ヒープ (Leftist Heap)
documentation_of: //DataStructure/Heap/LeftistHeap.py
---
## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $\mathrm{O}(1)$
- `min -> Any`  
ヒープ内の最小の値を返す。計算量 $\mathrm{O}(1)$
- `push(val: Any) -> None`  
ヒープに `val` を追加する。計算量 $\mathrm{O}(\log n)$
- `pop() -> Any`  
ヒープ内の最小の値を削除してその値を返す。計算量 $\mathrm{O}(\log n)$
- `meld(other: SkewHeap) -> None`  
ヒープに `other` を併合する。計算量 $\mathrm{O}(\log n)$
- `add(val: Any) -> None`  
ヒープ内のすべての要素に `val` を加算する。計算量 $\mathrm{O}(1)$
- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $\mathrm{O}(1)$
