---
title: Trie 木
documentation_of: //String/Trie.py
---

## 使い方
`Trie()`  
空の Trie 木を初期構築する。計算量 $O(1)$

- `search(string: str) -> bool`  
長さ $S$ の文字列 `string` が Trie 木に存在しているかどうかを返す。計算量 $O(S)$

- `insert(string: str) -> bool`  
長さ $S$ の文字列 `string` を Trie 木に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `string` が Trie 木に存在していた場合) は `False` を返す。計算量 $O(S)$ 

- `delete(string: str) -> bool`  
長さ $S$ の文字列 `string` を Trie 木から削除する。削除に成功した場合は `True` を、失敗した場合 (`string` が Trie 木に存在していなかった場合) は `False` を返す。計算量 $O(S)$
