---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_A.test.py
    title: TestCase\AOJ\DSL_2_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_B.SegTree.test.py
    title: TestCase\AOJ\DSL_2_B.SegTree.test.py
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
  code: "class SegmentTree:\r\n    def __init__(self, n, op, e):\r\n        self.n\
    \ = n\r\n        self.op = op\r\n        self.e = e\r\n        self.size = 2 **\
    \ ((n - 1).bit_length())\r\n        self.node = [self.e] * (2 * self.size)\r\n\
    \r\n    def __getitem__(self, i):\r\n        return self.node[i + self.size]\r\
    \n\r\n    def __setitem__(self, i, val):\r\n        i += self.size\r\n       \
    \ self.node[i] = val\r\n        while i > 1:\r\n            i >>= 1\r\n      \
    \      self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])\r\n\r\
    \n    def build(self, array):\r\n        for i, val in enumerate(array, self.size):\r\
    \n            self.node[i] = val\r\n        for i in range(self.size - 1, 0, -1):\r\
    \n            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])\r\
    \n\r\n    def all_fold(self):\r\n        return self.node[1]\r\n\r\n    def fold(self,\
    \ l, r):\r\n        l, r = l + self.size, r + self.size\r\n        vl, vr = self.e,\
    \ self.e\r\n        while l < r:\r\n            if l & 1:\r\n                vl\
    \ = self.op(vl, self.node[l])\r\n                l += 1\r\n            if r &\
    \ 1:\r\n                r -= 1\r\n                vr = self.op(self.node[r], vr)\r\
    \n            l, r = l >> 1, r >> 1\r\n        return self.op(vl, vr)\r\n\r\n\
    \    def max_right(self, l, f):\r\n        if l == self.n:\r\n            return\
    \ self.n\r\n        l += self.size\r\n        v = self.e\r\n        init = True\r\
    \n        while init or (l & -l) != l:\r\n            init = False\r\n       \
    \     while l % 2 == 0:\r\n                l >>= 1\r\n            if not f(self.op(v,\
    \ self.node[l])):\r\n                while l < self.size:\r\n                \
    \    l <<= 1\r\n                    if f(self.op(v, self.node[l])):\r\n      \
    \                  v = self.op(v, self.node[l])\r\n                        l +=\
    \ 1\r\n                return l - self.size\r\n            v = self.op(v, self.node[l])\r\
    \n            l += 1\r\n        return self.n\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\SegmentTree.py
  requiredBy: []
  timestamp: '2021-01-02 16:36:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_A.test.py
  - TestCase\AOJ\DSL_2_B.SegTree.test.py
documentation_of: DataStructure\SegmentTree\SegmentTree.py
layout: document
title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
---
