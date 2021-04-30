---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.ParingHeap.test.py
    title: TestCase/AOJ/ALDS1_9_C.ParingHeap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PHNode:\n    def __init__(self, val):\n        self.val = val\n   \
    \     self.chi = []\n\n\nclass ParingHeap:\n    def __init__(self):\n        self.root\
    \ = None\n\n    def empty(self):\n        return self.root is None\n\n    def\
    \ top(self):\n        return self.root.val\n\n    def push(self, val):\n     \
    \   self.root = self.merge(self.root, PHNode(val))\n\n    def pop(self):\n   \
    \     val = self.root.val\n        self.root = self.merge_pairs(self.root.chi)\n\
    \        return val\n\n    def merge(self, nd1, nd2):\n        if nd1 is None:\n\
    \            return nd2\n        elif nd2 is None:\n            return nd1\n \
    \       if nd1.val > nd2.val:\n            nd1, nd2 = nd2, nd1\n        nd1.chi.append(nd2)\n\
    \        return nd1\n\n    def merge_pairs(self, ndlist):\n        newlist = []\n\
    \        for i in range(len(ndlist) // 2):\n            newlist.append(self.merge(ndlist[i\
    \ * 2], ndlist[i * 2 + 1]))\n        if len(ndlist) % 2 == 0:\n            nd\
    \ = None\n        else:\n            nd = ndlist[-1]\n        for other in newlist:\n\
    \            nd = self.merge(nd, other)\n        return nd\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/ParingHeap.py
  requiredBy: []
  timestamp: '2021-01-04 23:38:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.ParingHeap.test.py
documentation_of: DataStructure/Heap/ParingHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Paring Heap)"
---
