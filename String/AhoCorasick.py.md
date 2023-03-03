---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0430.aho_corasick.test.py
    title: TestCase/yukicoder/yuki0430.aho_corasick.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from collections import deque\nfrom standard_library.collections import\
    \ deque\n\n\nclass Node:\n    def __init__(self):\n        self.child = {}\n \
    \       self.failure = None\n        self.valid = 0\n\n    def set_child(self,\
    \ s):\n        self.child[s] = Node()\n\n    def get_child(self, s):\n       \
    \ if s not in self.child:\n            return None\n        return self.child[s]\n\
    \n\nclass AhoCorasick:\n    def __init__(self):\n        self.root = Node()\n\n\
    \    def add(self, pattern):\n        ptr = self.root\n        for s in pattern:\n\
    \            if ptr.get_child(s) is None:\n                ptr.set_child(s)\n\
    \            ptr = ptr.get_child(s)\n        ptr.valid += 1\n\n    def build_pma(self):\n\
    \        queue = deque()\n        for s in self.root.child:\n            ptrch\
    \ = self.root.child[s]\n            ptrch.failure = self.root\n            queue.append(ptrch)\n\
    \        while queue:\n            ptr = queue.popleft()\n            ptr.valid\
    \ += ptr.failure.valid\n            for s in ptr.child:\n                ptrch\
    \ = ptr.child[s]\n                f = ptr.failure\n                while f is\
    \ not None and f.get_child(s) is None:\n                    f = f.failure\n  \
    \              ptrch.failure = f.get_child(s) if f is not None else self.root\n\
    \                queue.append(ptrch)\n\n    def match_count(self, text):\n   \
    \     ptr = self.root\n        res = 0\n        for s in text:\n            while\
    \ ptr is not None and ptr.get_child(s) is None:\n                ptr = ptr.failure\n\
    \            ptr = ptr.get_child(s) if ptr is not None else self.root\n      \
    \      res += ptr.valid\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: String/AhoCorasick.py
  requiredBy: []
  timestamp: '2022-01-22 12:11:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0430.aho_corasick.test.py
documentation_of: String/AhoCorasick.py
layout: document
title: "Aho-Corasick \u6CD5"
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
