---
title: 併合可能永続ヒープ (Persistent Leftist Heap)
documentation_of: //DataStructure/Heap/PersistentLeftistHeap.py
---

## 概要
大きさが $N$ と $M$ のヒープ同士を計算量 $O(\log (N+M))$ で併合可能な永続ヒープ。ヒープの要素は (キー, 値) の組み合わせで表現され、キーの小さい要素が優先度が高い。キーは重複を許す。

## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $O(1)$

- `__bool__() -> bool`  
ヒープが空かどうか返す。計算量 $O(1)$

- `__lt__(other: LeftistHeap) -> bool`  
ヒープ同士をキーの値で比較し、`other` よりも小さければ `True` を返す。そうでなければ `False` を返す。計算量 $O(1)$

- `insert(key: int, val: int) -> LeftistHeap`  
ヒープに (キー、 値) の組を持つ要素を追加したときのヒープを返す。ヒープの大きさを $N$ とすると、計算量 $O(\log N)$

- `find_min -> Tuple[int, int]`  
ヒープ内の最小のキーを持つ要素の (キー, 値) の組を返す。計算量 $O(1)$

- `delete_min() -> LeftistHeap`  
ヒープ内の最小のキーを持つ要素を $1$ つ削除したときのヒープを返す。ヒープの大きさを $N$ とすると、計算量 $O(\log N)$

`LeftistHeap.merge(hl: LeftistHeap, hr: LeftistHeap) -> LeftistHeap`  
ヒープ `hl` と `hr` を併合したときのヒープを返す。それぞれのヒープの大きさを $N, M$ とすると、計算量 $O(\log(N+M))$
