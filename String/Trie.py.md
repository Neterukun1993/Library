---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0430.test.py
    title: TestCase/yukicoder/yuki0430.test.py
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
  code: "class TrieNode:\n    def __init__(self):\n        self.child = {}\n     \
    \   self.valid = False\n\n    def set_child(self, s):\n        self.child[s] =\
    \ TrieNode()\n\n    def get_child(self, s):\n        if s not in self.child:\n\
    \            return None\n        return self.child[s]\n\n\nclass Trie:\n    def\
    \ __init__(self):\n        self.root = TrieNode()\n\n    def search(self, string):\n\
    \        ptr = self.root\n        for s in string:\n            if ptr.get_child(s)\
    \ is None:\n                return False\n            ptr = ptr.get_child(s)\n\
    \        return ptr.valid\n\n    def insert(self, string):\n        ptr = self.root\n\
    \        for s in string:\n            if ptr.get_child(s) is None:\n        \
    \        ptr.set_child(s)\n            ptr = ptr.get_child(s)\n        if ptr.valid:\n\
    \            return False\n        ptr.valid = True\n        return True\n\n \
    \   def delete(self, string):\n        ptr = self.root\n        for s in string:\n\
    \            if ptr.get_child(s) is None:\n                return False\n    \
    \        ptr = ptr.get_child(s)\n        ptr.valid = False\n        return True\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Trie.py
  requiredBy: []
  timestamp: '2021-05-24 02:37:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0430.test.py
documentation_of: String/Trie.py
layout: document
title: "Trie \u6728"
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
