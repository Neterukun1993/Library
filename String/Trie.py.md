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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class TrieNode:\n    def __init__(self, s):\n        self.child = {}\n  \
    \      self.valid = False\n\n    def set_child(self, s):\n        self.child[s]\
    \ = TrieNode(s)\n\n    def get_child(self, s):\n        if s not in self.child:\n\
    \            return None\n        return self.child[s]\n\n\nclass Trie:\n    def\
    \ __init__(self):\n        self.root = TrieNode(None)\n\n    def search(self,\
    \ string: str) -> bool:\n        ptr = self.root\n        for s in string:\n \
    \           if ptr.get_child(s) is None:\n                return False\n     \
    \       ptr = ptr.get_child(s)\n        return ptr.valid\n\n    def insert(self,\
    \ string: str):\n        ptr = self.root\n        for s in string:\n         \
    \   if ptr.get_child(s) is None:\n                ptr.set_child(s)\n         \
    \   ptr = ptr.get_child(s)\n        ptr.valid = True\n\n    def delete(self, string:\
    \ str):\n        ptr = self.root\n        for s in string:\n            if ptr.get_child(s)\
    \ is None:\n                return\n            ptr = ptr.get_child(s)\n     \
    \   ptr.valid = False\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Trie.py
  requiredBy: []
  timestamp: '2021-01-16 14:01:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0430.test.py
documentation_of: String/Trie.py
layout: document
title: "Trie\u6728"
---
