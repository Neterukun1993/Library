---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0430.Patricia.test.py
    title: TestCase/yukicoder/yuki0430.Patricia.test.py
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
  code: "class PatriciaNode:\n    def __init__(self, string=None):\n        self.data\
    \ = string\n        self.child = {}\n        self.valid = False\n\n    def set_child(self,\
    \ string):\n        self.child[string[0]] = PatriciaNode(string)\n        return\
    \ self.child[string[0]]\n\n    def get_child(self, s):\n        if s not in self.child:\n\
    \            return None\n        return self.child[s]\n\n\nclass Patricia:\n\
    \    def __init__(self):\n        self.root = PatriciaNode()\n\n    def _longest_match(self,\
    \ string):\n        ptr = self.root\n        i = 0\n        while i < len(string):\n\
    \            ptrch = ptr.get_child(string[i])\n            if ptrch is None:\n\
    \                break\n            j = 1\n            while j < len(ptrch .data):\n\
    \                if i + j == len(string) or string[i + j] != ptrch.data[j]:\n\
    \                    return ptrch, i + j, j\n                j += 1\n        \
    \    i += j\n            ptr = ptrch\n        return ptr, i, 0\n\n    def search(self,\
    \ string):\n        ptr, match, sub_match = self._longest_match(string)\n    \
    \    if len(string) == match and sub_match == 0:\n            return ptr.valid\n\
    \        return False\n\n    def insert(self, string):\n        ptr, match, sub_match\
    \ = self._longest_match(string)\n        if len(string) == match and sub_match\
    \ == 0 and ptr.valid:\n            return False\n        if sub_match > 0:\n \
    \           newptr = PatriciaNode(ptr.data[sub_match:])\n            newptr.child\
    \ = ptr.child\n            newptr.valid = ptr.valid\n            ptr.data = ptr.data[:sub_match]\n\
    \            ptr.child = {newptr.data[0]: newptr}\n            ptr.valid = False\n\
    \        if match < len(string):\n            ptr = ptr.set_child(string[match:])\n\
    \        ptr.valid = True\n        return True\n\n    def delete(self, string):\n\
    \        ptr, match, sub_match = self._longest_match(string)\n        if len(string)\
    \ == match and sub_match == 0 and ptr.valid:\n            ptr.valid = False\n\
    \            return True\n        return False\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Patricia.py
  requiredBy: []
  timestamp: '2021-05-24 02:37:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0430.Patricia.test.py
documentation_of: String/Patricia.py
layout: document
title: "Patricia \u6728"
---

## 使い方
`Patricia()`  
空の Patricia 木を初期構築する。計算量 $O(1)$

- `search(string: str) -> bool`  
長さ $S$ の文字列 `string` が Patricia 木に存在しているかどうかを返す。計算量 $O(S)$

- `insert(string: str) -> bool`  
長さ $S$ の文字列 `string` を Patricia 木に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `string` が Patricia 木に存在していた場合) は `False` を返す。計算量 $O(S)$ 

- `delete(string: str) -> bool`  
長さ $S$ の文字列 `string` を Patricia 木から削除する。削除に成功した場合は `True` を、失敗した場合 (`string` が Patricia 木に存在していなかった場合) は `False` を返す。計算量 $O(S)$
