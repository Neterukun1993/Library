---
title: Aho-Corasick 法
documentation_of: //String/AhoCorasick.py
---

## 使い方
`AhoCorasick()`  
空の Trie 木を初期構築する。計算量 $O(1)$

- `add(pattern: str) -> None`  
パターン文字列 $P$ (`pattern`) を Trie 木に追加する。計算量 $O(|P|)$

- `build_pma() -> None`  
Trie 木に追加されたパターン文字列 $P_0, P_1, \cdots, Pn$ 対してパターンマッチングオートマトンを構築する。計算量 $O(\sum |P_i|)$

- `match_count(text: str) -> int`  
テキスト文字列 $T$ (`text`) に現れるパターン文字列の総数を返す。計算量 $O(|T|)$
