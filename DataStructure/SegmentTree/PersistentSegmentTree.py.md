---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PSTNode:\n    def __init__(self, val):\n        self.val = val\n  \
    \      self.l = None\n        self.r = None\n\n\nclass PersistentSegmentTree:\n\
    \    def __init__(self, op, e, root=None):\n        self.op = op\n        self.e\
    \ = e\n        self.root = root\n\n    def build(self, array):\n        n = len(array)\n\
    \        self.log = (n - 1).bit_length()\n        self.size = 2 ** self.log\n\
    \        array = [PSTNode(array[i] if i < n else self.e) for i in range(self.size)]\n\
    \        tmp = []\n        for h in range(self.log):\n            for i in range(1\
    \ << (self.log - h - 1)):\n                nd = self.make_parent(array[i << 1\
    \ | 0], array[i << 1 | 1])\n                tmp.append(nd)\n            array,\
    \ tmp = tmp, array\n        self.root = array[0]\n\n    def __getitem__(self,\
    \ i):\n        nd = self.root\n        for h in range(self.log):\n           \
    \ if (i >> (self.log - h - 1)) & 1:\n                nd = nd.r\n            else:\n\
    \                nd = nd.l\n        return nd.val\n\n    def update(self, i, val):\n\
    \        nd = self.root\n        stack = []\n        for h in range(self.log):\n\
    \            stack.append(nd)\n            if (i >> (self.log - h - 1)) & 1:\n\
    \                nd = nd.r\n            else:\n                nd = nd.l\n   \
    \     nd = PSTNode(val)\n        for ndp in reversed(stack):\n            if ndp.l\
    \ is nd:\n                nd = make_parent(nd, nd.r)\n            else:\n    \
    \            nd = make_parent(nd.l, nd)\n        return PersistentSegmentTree(self.op,\
    \ self.e, nd)\n\n    def make_parent(self, ndl, ndr):\n        val = self.op(ndl.val,\
    \ ndr.val)\n        nd = PSTNode(val)\n        nd.l, nd.r = ndl, ndr\n       \
    \ return nd\n\n    def all_fold(self):\n        return self.root.val\n\n    def\
    \ fold(self, l, r):\n        return self._fold(l, r, 0, self.n, self.root)\n\n\
    \    def _fold(self, a, b, k, l, r, nd):\n        if r <= a or b <= l:\n     \
    \       return self.e\n        if a <= l and r <= b:\n            return self.nd.val\n\
    \        vl = self._fold(a, b, l, (l + r) >> 1, nd.l)\n        vr = self._fold(a,\
    \ b, (l + r) >> 1, r, nd.r)\n        return self.op(vl, vr)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/PersistentSegmentTree.py
  requiredBy: []
  timestamp: '2021-02-03 22:47:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/PersistentSegmentTree.py
layout: document
title: "\u6C38\u7D9A\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---
