---
title: 両端キュー (循環バッファ/ランダムアクセス$O(1)$)
documentation_of: //DataStructure/misc/ArrayDeque.py
---

## 概要
ランダムアクセスが $O(1)$ で可能な両端キュー。

## 使い方
`ArrayDeque()`  
空の両端キューを構築する。計算量 $O(1)$

- `__len__() -> int`  
両端キューの大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[Any]`  
先頭のイテレータオブジェクトを返す。計算量 $O(1)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(1)$

- `__setitem__(i: int, val: Any) -> None`  
`i` 番目の要素を `val` に変更する。計算量 $O(1)$

- `append(val: Any) -> None`  
両端キューの末尾に要素 `val` を追加する。計算量 $\mathrm{amortized}\ O(1)$

- `appendleft(val: Any) -> None`  
両端キューの先頭に要素 `val` を追加する。計算量 $\mathrm{amortized}\ O(1)$

- `pop() -> Any`  
両端キューの末尾要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$

- `popleft() -> Any`  
両端キューの先頭要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$

- `clear() -> None`  
両端キューを空にする。計算量 $O(1)$
