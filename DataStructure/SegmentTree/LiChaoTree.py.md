---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\line_add_get_min.test.py
    title: TestCase\LibraryChecker\line_add_get_min.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\segment_add_get_min.test.py
    title: TestCase\LibraryChecker\segment_add_get_min.test.py
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
  code: "from bisect import bisect_left\r\n\r\n\r\nclass LiChaoTree:\r\n    def __init__(self,\
    \ xs, INF=10**18):\r\n        self.INF = INF\r\n        xs = sorted(list(set(xs)))\r\
    \n        n = len(xs)\r\n        self.size = 1 << (n - 1).bit_length()\r\n   \
    \     self.comp_xs = {x: ind for ind, x in enumerate(xs)}\r\n        self.xs =\
    \ xs + [self.INF] * (self.size - n)\r\n        self.data = [None] * (self.size\
    \ + self.size)\r\n\r\n    def update(self, line, k, l, r):\r\n        while True:\r\
    \n            if self.data[k] is None:\r\n                self.data[k] = line\r\
    \n                return\r\n            mid = (l + r) >> 1\r\n            lx,\
    \ mx, rx = self.xs[l], self.xs[mid], self.xs[r - 1]\r\n            lu = self.f(line,\
    \ lx) < self.f(self.data[k], lx)\r\n            mu = self.f(line, mx) < self.f(self.data[k],\
    \ mx)\r\n            ru = self.f(line, rx) < self.f(self.data[k], rx)\r\n    \
    \        if lu and ru:\r\n                self.data[k] = line\r\n            \
    \    return\r\n            if not lu and not ru:\r\n                return\r\n\
    \            if mu:\r\n                self.data[k], line = line, self.data[k]\r\
    \n            if lu != mu:\r\n                r, k = mid, k << 1\r\n         \
    \   else:\r\n                l, k = mid, k << 1 | 1\r\n\r\n    def add_line(self,\
    \ line):\r\n        self.update(line, 1, 0, self.size)\r\n\r\n    def add_seg(self,\
    \ line, l, r):\r\n        l = bisect_left(self.xs, l)\r\n        r = bisect_left(self.xs,\
    \ r)\r\n        l0, r0 = l + self.size, r + self.size\r\n        size = 1\r\n\
    \        while l0 < r0:\r\n            if l0 & 1:\r\n                self.update(line,\
    \ l0, l, l + size)\r\n                l0 += 1\r\n                l += size\r\n\
    \            if r0 & 1:\r\n                r0 -= 1\r\n                r -= size\r\
    \n                self.update(line, r0, r, r + size)\r\n            l0 >>= 1\r\
    \n            r0 >>= 1\r\n            size <<= 1\r\n\r\n    def f(self, line,\
    \ x):\r\n        a, b = line\r\n        return a * x + b\r\n\r\n    def min(self,\
    \ x):\r\n        k = self.comp_xs[x] + self.size\r\n        res = self.INF\r\n\
    \        while k > 0:\r\n            if self.data[k] is not None:\r\n        \
    \        res = min(res, self.f(self.data[k], x))\r\n            k >>= 1\r\n  \
    \      return res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\LiChaoTree.py
  requiredBy: []
  timestamp: '2021-01-03 06:18:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\line_add_get_min.test.py
  - TestCase\LibraryChecker\segment_add_get_min.test.py
documentation_of: DataStructure\SegmentTree\LiChaoTree.py
layout: document
title: Li-Chao Tree
---
