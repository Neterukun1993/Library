---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
    title: TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SuffixAutomaton:\n    def __init__(self):\n        self.last = 0\n\
    \        self.next = [{}]\n        self.link = [-1]\n        self.length = [0]\n\
    \n    def _add_node(self, link, length):\n        self.next.append({})\n     \
    \   self.link.append(link)\n        self.length.append(length)\n\n    def push(self,\
    \ char):\n        nxt, link, length = self.next, self.link, self.length\n    \
    \    new_node = len(nxt)\n        self._add_node(-1, length[self.last] + 1)\n\
    \        p = self.last\n        while p != -1 and char not in nxt[p]:\n      \
    \      nxt[p][char] = new_node\n            p = link[p]\n        q = 0 if p ==\
    \ -1 else nxt[p][char]\n        if p == -1 or length[p] + 1 == length[q]:\n  \
    \          link[new_node] = q\n        else:\n            new_q = len(nxt)\n \
    \           self._add_node(link[q], length[p] + 1)\n            nxt[-1] = {c:\
    \ nxt[q][c] for c in nxt[q]}\n            link[q] = link[new_node] = new_q\n \
    \           while p != -1 and nxt[p][char] == q:\n                nxt[p][char]\
    \ = new_q\n                p = link[p]\n        self.last = new_node\n\n    def\
    \ has_substring(self, pattern):\n        p = 0\n        for char in pattern:\n\
    \            if char not in self.next[p]:\n                return False\n    \
    \        p = self.next[p][char]\n        return True\n\n    def number_of_substrings(self):\n\
    \        ans = 0\n        for i in range(1, len(self.length)):\n            ans\
    \ += self.length[i] - self.length[self.link[i]]\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: String/SuffixAutomaton.py
  requiredBy: []
  timestamp: '2021-06-13 17:43:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/number_of_substrings.suffix_automaton.test.py
documentation_of: String/SuffixAutomaton.py
layout: document
title: Suffix automaton
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
