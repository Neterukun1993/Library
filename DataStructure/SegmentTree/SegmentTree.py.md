---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_A.test.py
    title: TestCase/AOJ/DSL_2_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_B.SegTree.test.py
    title: TestCase/AOJ/DSL_2_B.SegTree.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegmentTree:\n    def __init__(self, n, op, e):\n        self.n = n\n\
    \        self.op = op\n        self.e = e\n        self.size = 2 ** ((n - 1).bit_length())\n\
    \        self.node = [self.e] * (2 * self.size)\n\n    def __getitem__(self, i):\n\
    \        return self.node[i + self.size]\n\n    def __setitem__(self, i, val):\n\
    \        i += self.size\n        self.node[i] = val\n        while i > 1:\n  \
    \          i >>= 1\n            self.node[i] = self.op(self.node[i << 1], self.node[(i\
    \ << 1) + 1])\n\n    def build(self, array):\n        for i, val in enumerate(array,\
    \ self.size):\n            self.node[i] = val\n        for i in range(self.size\
    \ - 1, 0, -1):\n            self.node[i] = self.op(self.node[i << 1], self.node[(i\
    \ << 1) + 1])\n\n    def all_fold(self):\n        return self.node[1]\n\n    def\
    \ fold(self, l, r):\n        l, r = l + self.size, r + self.size\n        vl,\
    \ vr = self.e, self.e\n        while l < r:\n            if l & 1:\n         \
    \       vl = self.op(vl, self.node[l])\n                l += 1\n            if\
    \ r & 1:\n                r -= 1\n                vr = self.op(self.node[r], vr)\n\
    \            l, r = l >> 1, r >> 1\n        return self.op(vl, vr)\n\n    def\
    \ max_right(self, l, f):\n        if l == self.n:\n            return self.n\n\
    \        l += self.size\n        v = self.e\n        init = True\n        while\
    \ init or (l & -l) != l:\n            init = False\n            while l % 2 ==\
    \ 0:\n                l >>= 1\n            if not f(self.op(v, self.node[l])):\n\
    \                while l < self.size:\n                    l <<= 1\n         \
    \           if f(self.op(v, self.node[l])):\n                        v = self.op(v,\
    \ self.node[l])\n                        l += 1\n                return l - self.size\n\
    \            v = self.op(v, self.node[l])\n            l += 1\n        return\
    \ self.n\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/SegmentTree.py
  requiredBy: []
  timestamp: '2021-01-02 16:36:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_A.test.py
  - TestCase/AOJ/DSL_2_B.SegTree.test.py
documentation_of: DataStructure/SegmentTree/SegmentTree.py
layout: document
title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
---