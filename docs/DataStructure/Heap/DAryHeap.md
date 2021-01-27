---
title: D-Ary Heap
documentation_of: //DataStructure/Heap/DAryHeap.py
---
## 概要
二分ヒープ (Binary Heap) を `D` 分木に拡張したヒープ。`D = 2` であれば Binary Heap、`D = 3` であれば Ternary Heap、`D = 4` であれば Quaternary Heap。子 `k` から親へのアクセスおよび親 `k` から子へのアクセスを添え字で表現できるため、配列上でヒープをシミュレートできる。

画像は D-Ary Heap の添字の様子。
![example]("https://Neterukun1993.github.io/Library/DAryHeap-example.png")
![index]("https://Neterukun1993.github.io/Library/DAryHeap-index.png")

## 使い方
`DAryHeap(D: int)`  
`D` 分木版の空の Binary Heap を作成する。計算量 $O(1)$

- `__len__() -> int`  
ヒープの大きさを返す。計算量 $O(1)$

- `min -> Any`  
ヒープ内の最小の値を返す。計算量 $O(1)$

- `push(val: Any) -> None`  
ヒープに `val` を追加する。計算量 $O(\log n / \log D)$

- `pop() -> Any`  
ヒープ内の最小の値を削除してその値を返す。計算量 $O(D\log n / \log D$
