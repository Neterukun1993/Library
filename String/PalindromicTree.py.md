---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0263.test.py
    title: TestCase/yukicoder/yuki0263.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://math314.hateblo.jp/entry/2016/12/19/005919
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# PalindromicTree\n# https://math314.hateblo.jp/entry/2016/12/19/005919\n\
    \nclass Node:\n    def __init__(self, length, count):\n        self.length = length\n\
    \        self.count = count\n        self.suffix_link = 0\n        self.link =\
    \ {}\n\n\nclass PalindromicTree:\n    def __init__(self):\n        self.nodes\
    \ = []\n        self.string = []\n\n        self.root_odd = Node(-1, 0)\n    \
    \    self.nodes.append(self.root_odd)\n        self.root_even = Node(0, 0)\n \
    \       self.nodes.append(self.root_even)\n        self.cur = 0\n\n    def prev_palindrome_node(self,\
    \ idx):\n        size = len(self.string) - 1\n        while True:\n          \
    \  i = size - 1 - self.nodes[idx].length\n            if i >= 0 and self.string[i]\
    \ == self.string[-1]:\n                break\n            idx = self.nodes[idx].suffix_link\n\
    \        return idx\n\n    def add(self, char):\n        self.string.append(char)\n\
    \        idx = self.prev_palindrome_node(self.cur)\n\n        if char in self.nodes[idx].link:\n\
    \            self.cur = self.nodes[idx].link[char]\n            self.nodes[self.cur].count\
    \ += 1\n            return\n\n        self.nodes[idx].link[char] = len(self.nodes)\n\
    \        new = Node(self.nodes[idx].length + 2, 1)\n        self.nodes.append(new)\n\
    \        self.cur = self.nodes[idx].link[char]\n\n        if new.length == 1:\n\
    \            new.suffix_link = 1\n        else:\n            idx = self.prev_palindrome_node(self.nodes[idx].suffix_link)\n\
    \            new.suffix_link = self.nodes[idx].link[char]\n\n    def frequency_build(self):\n\
    \        n = len(self.nodes)\n        frequency = [0] * n\n        for i in reversed(range(n)):\n\
    \            frequency[i] += self.nodes[i].count\n            frequency[self.nodes[i].suffix_link]\
    \ += frequency[i]\n        return frequency\n"
  dependsOn: []
  isVerificationFile: false
  path: String/PalindromicTree.py
  requiredBy: []
  timestamp: '2021-10-04 23:59:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0263.test.py
documentation_of: String/PalindromicTree.py
layout: document
title: "\u56DE\u5206\u6728 (Palindrome tree)"
---
