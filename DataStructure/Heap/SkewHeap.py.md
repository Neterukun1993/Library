---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
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
    \    self.r = None\n        self.val = val\n\n\nclass SkewHeap:\n    def __init__(self):\n\
    \        self.root = None\n\n    def _meld(self, a, b):\n        if a is None:\n\
    \            return b\n        elif b is None:\n            return a\n       \
    \ if b.val < a.val:\n            a, b = b, a\n        a.r = self._meld(a.r, b)\n\
    \        a.l, a.r = a.r, a.l\n        return a\n\n    def push(self, val):\n \
    \       nd = SHNode(val)\n        self.root = self._meld(self.root, nd)\n\n  \
    \  def pop(self):\n        rt = self.root\n        self.root = self._meld(rt.l,\
    \ rt.r)\n        return rt.val\n\n    def meld(self, other):\n        sh = SkewHeap()\n\
    \        sh.root = self._meld(self.root, other.root)\n        return sh\n\n  \
    \  def empty(self):\n        return self.root is None\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/SkewHeap.py
  requiredBy: []
  timestamp: '2021-01-04 23:38:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
documentation_of: DataStructure/Heap/SkewHeap.py
layout: document
redirect_from:
- /library/DataStructure/Heap/SkewHeap.py
- /library/DataStructure/Heap/SkewHeap.py.html
title: DataStructure/Heap/SkewHeap.py
---
