---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedSetBTree.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (B-Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_D.BTree.test.py
    title: TestCase/AOJ/ITP2_7_D.BTree.test.py
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
  code: "from bisect import bisect_left, bisect_right, insort\nfrom DataStructure.SortedSet.SortedSetBTree\
    \ import BTreeNode, SortedSetBTree\n\n\nclass SortedMultiSetBTree(SortedSetBTree):\n\
    \    def __init__(self, B_SIZE=512):\n        super().__init__(B_SIZE)\n\n   \
    \ def add(self, key):\n        ptr = self.root\n        p = self._add_rec(ptr,\
    \ key)\n        if p is not None:\n            root = BTreeNode(self.B_SIZE)\n\
    \            root.keys = [p.keys.pop()]\n            root.children = [p, self.root]\n\
    \            self.root = root\n        self.size += 1\n        return True\n"
  dependsOn:
  - DataStructure/SortedSet/SortedSetBTree.py
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedMultiSetBTree.py
  requiredBy: []
  timestamp: '2021-02-07 17:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_D.BTree.test.py
documentation_of: DataStructure/SortedSet/SortedMultiSetBTree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u591A\u91CD\u96C6\u5408 (B-Tree)"
---
## 概要
B-Tree による順序付き多重集合。
