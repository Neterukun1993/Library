---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/SpanningTree/directed_mst.py
    title: "\u6700\u5C0F\u6709\u5411\u5168\u57DF\u6728"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
    title: TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SHNode:\n    def __init__(self, val):\n        self.l = None\n    \
    \    self.r = None\n        self.val = val\n        self.add = 0\n\n    def lazy_propagate(self):\n\
    \        if self.l is not None: self.l.add += self.add\n        if self.r is not\
    \ None: self.r.add += self.add\n        self.val += self.add\n        self.add\
    \ = 0\n\n\nclass SkewHeap:\n    def __init__(self):\n        self.root = None\n\
    \n    def _meld(self, a, b):\n        if a is None: return b\n        if b is\
    \ None: return a\n        if b.val + b.add < a.val + a.add: a, b = b, a\n    \
    \    a.lazy_propagate()\n        a.r = self._meld(a.r, b)\n        a.l, a.r =\
    \ a.r, a.l\n        return a\n\n    @ property\n    def min(self):\n        self.root.lazy_propagate()\n\
    \        return self.root.val\n\n    def push(self, val):\n        nd = SHNode(val)\n\
    \        self.root = self._meld(self.root, nd)\n\n    def pop(self):\n       \
    \ rt = self.root\n        rt.lazy_propagate()\n        self.root = self._meld(rt.l,\
    \ rt.r)\n        return rt.val\n\n    def meld(self, other):\n        self.root\
    \ = self._meld(self.root, other.root)\n\n    def add(self, val):\n        self.root.add\
    \ += val\n\n    def empty(self):\n        return self.root is None\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/SkewHeap.py
  requiredBy:
  - Graph/SpanningTree/directed_mst.py
  timestamp: '2021-01-14 12:29:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
documentation_of: DataStructure/Heap/SkewHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Skew Heap)"
---