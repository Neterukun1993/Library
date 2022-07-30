---
title: 対数時間ランダムアクセス/挿入/削除可能リスト (UnrolledLinkedList)
documentation_of: //DataStructure/List/UnrolledLinkedList.py
---

## 概要
要素のランダムアクセスを、挿入、削除を行えるリスト。

## 使い方
`UnrolledLinkedList()`  
空のリストを作成する。計算量 $O(1)$。それぞれのノードに含めることができる最大の要素数を $L(=4096)$ とする。

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(N/L)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を代入する。計算量 $O(N/L)$

- `__len__() -> int`  
リストの長さを返す。計算量 $O(1)$

- `insert(i: int, val: int) -> None`  
$i$ 番目の位置に `val` を挿入する。計算量 $O(N/L + L)$

- `delete(i: int) -> None`  
$i$ 番目の要素を削除する。計算量 $O(N/L + L)$

- `dump() -> List[int]`  
リストの要素を列挙した結果を返す。計算量 $O(N)$

## 参考
[Unrolled linked list - Wikipedia](https://ja.wikipedia.org/wiki/Unrolled_linked_list)
