---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0430.test.py
    title: TestCase\yukicoder\yuki0430.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class TrieNode:\r\n    def __init__(self, s):\r\n        self.child = {}\r\
    \n        self.valid = False\r\n\r\n    def set_child(self, s):\r\n        self.child[s]\
    \ = TrieNode(s)\r\n\r\n    def get_child(self, s):\r\n        if s not in self.child:\r\
    \n            return None\r\n        return self.child[s]\r\n\r\n\r\nclass Trie:\r\
    \n    def __init__(self):\r\n        self.root = TrieNode(None)\r\n\r\n    def\
    \ search(self, string: str) -> bool:\r\n        ptr = self.root\r\n        for\
    \ s in string:\r\n            if ptr.get_child(s) is None:\r\n               \
    \ return False\r\n            ptr = ptr.get_child(s)\r\n        return ptr.valid\r\
    \n\r\n    def insert(self, string: str):\r\n        ptr = self.root\r\n      \
    \  for s in string:\r\n            if ptr.get_child(s) is None:\r\n          \
    \      ptr.set_child(s)\r\n            ptr = ptr.get_child(s)\r\n        ptr.valid\
    \ = True\r\n\r\n    def delete(self, string: str):\r\n        ptr = self.root\r\
    \n        for s in string:\r\n            if ptr.get_child(s) is None:\r\n   \
    \             return\r\n            ptr = ptr.get_child(s)\r\n        ptr.valid\
    \ = False\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\Trie.py
  requiredBy: []
  timestamp: '2021-01-16 14:01:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\yukicoder\yuki0430.test.py
documentation_of: String\Trie.py
layout: document
title: "Trie\u6728"
---
