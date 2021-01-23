---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: misc\xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.RandomizedMeldableHeap.test.py
    title: TestCase\AOJ\ALDS1_9_C.RandomizedMeldableHeap.test.py
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
  code: "from misc.xorshift import xorshift32\r\n\r\n\r\nrand32 = xorshift32()\r\n\
    \r\n\r\nclass RMHNode:\r\n    def __init__(self, val):\r\n        self.l = None\r\
    \n        self.r = None\r\n        self.val = val\r\n\r\n\r\nclass RandomizedMeldableHeap:\r\
    \n    def __init__(self):\r\n        self.root = None\r\n\r\n    def _meld(self,\
    \ a, b):\r\n        if a is None: return b\r\n        if b is None: return a\r\
    \n        if b.val < a.val: a, b = b, a\r\n        if rand32() & 1:\r\n      \
    \      a.l = self._meld(a.l, b)\r\n        else:\r\n            a.r = self._meld(a.r,\
    \ b)\r\n        return a\r\n\r\n    @ property\r\n    def min(self):\r\n     \
    \   return self.root.val\r\n\r\n    def push(self, val):\r\n        nd = RMHNode(val)\r\
    \n        self.root = self._meld(self.root, nd)\r\n\r\n    def pop(self):\r\n\
    \        rt = self.root\r\n        self.root = self._meld(rt.l, rt.r)\r\n    \
    \    return rt.val\r\n\r\n    def meld(self, other):\r\n        self.root = self._meld(self.root,\
    \ other.root)\r\n\r\n    def empty(self):\r\n        return self.root is None\r\
    \n"
  dependsOn:
  - misc\xorshift.py
  isVerificationFile: false
  path: DataStructure\Heap\RandomizedMeldableHeap.py
  requiredBy: []
  timestamp: '2021-01-19 22:36:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_9_C.RandomizedMeldableHeap.test.py
documentation_of: DataStructure\Heap\RandomizedMeldableHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Randomized Meldable Heap)"
---
