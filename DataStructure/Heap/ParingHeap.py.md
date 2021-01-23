---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_9_C.ParingHeap.test.py
    title: TestCase\AOJ\ALDS1_9_C.ParingHeap.test.py
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
  code: "class PHNode:\r\n    def __init__(self, val):\r\n        self.val = val\r\
    \n        self.chi = []\r\n\r\n\r\nclass ParingHeap:\r\n    def __init__(self):\r\
    \n        self.root = None\r\n\r\n    def empty(self):\r\n        return self.root\
    \ is None\r\n\r\n    def top(self):\r\n        return self.root.val\r\n\r\n  \
    \  def push(self, val):\r\n        self.root = self.merge(self.root, PHNode(val))\r\
    \n\r\n    def pop(self):\r\n        val = self.root.val\r\n        self.root =\
    \ self.merge_pairs(self.root.chi)\r\n        return val\r\n\r\n    def merge(self,\
    \ nd1, nd2):\r\n        if nd1 is None:\r\n            return nd2\r\n        elif\
    \ nd2 is None:\r\n            return nd1\r\n        if nd1.val > nd2.val:\r\n\
    \            nd1, nd2 = nd2, nd1\r\n        nd1.chi.append(nd2)\r\n        return\
    \ nd1\r\n\r\n    def merge_pairs(self, ndlist):\r\n        newlist = []\r\n  \
    \      for i in range(len(ndlist) // 2):\r\n            newlist.append(self.merge(ndlist[i\
    \ * 2], ndlist[i * 2 + 1]))\r\n        if len(ndlist) % 2 == 0:\r\n          \
    \  nd = None\r\n        else:\r\n            nd = ndlist[-1]\r\n        for other\
    \ in newlist:\r\n            nd = self.merge(nd, other)\r\n        return nd\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\Heap\ParingHeap.py
  requiredBy: []
  timestamp: '2021-01-04 23:38:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_9_C.ParingHeap.test.py
documentation_of: DataStructure\Heap\ParingHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Paring Heap)"
---
