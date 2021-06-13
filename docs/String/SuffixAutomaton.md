---
title: Suffix automaton
documentation_of: //String/SuffixAutomaton.py
---

## 使い方
`SuffixAutomaton()`  
空文字列 $S$ に対する suffix automaton を構築する。計算量 $O(1)$

- `push(char: str)`  
文字列 $S$ の末尾に 1 文字 `char` を追加し、suffix automaton を更新する。計算量 $O(1)$

- `has_substring(pattern: str)`  
文字列 $S$ にパターン文字列 $P$ (`pattern`) が部分文字列として存在するかどうか返す。計算量 $O(|P|)$

- `number_of_substrings() -> int`  
文字列 $S$ の相異なる部分文字列の個数を返す。計算量 $O(|S|)$
