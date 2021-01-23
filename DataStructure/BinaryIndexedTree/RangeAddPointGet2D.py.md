---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_5_B.BIT.test.py
    title: TestCase\AOJ\DSL_5_B.BIT.test.py
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
  code: "class BinaryIndexedTree:\r\n    def __init__(self, h, w):\r\n        self.h\
    \ = h\r\n        self.w = w\r\n        self.bit = [[0] * (self.w + 1) for _ in\
    \ range(self.h + 1)]\r\n\r\n    def __getitem__(self, ij):\r\n        i, j0 =\
    \ ij\r\n        i = i + 1\r\n        s = 0\r\n        while i <= self.h:\r\n \
    \           j = j0 + 1\r\n            while j <= self.w:\r\n                s\
    \ += self.bit[i][j]\r\n                j += j & -j\r\n            i += i & -i\r\
    \n        return s\r\n\r\n    def _add(self, i, j, val):\r\n        j0 = j\r\n\
    \        while i > 0:\r\n            j = j0\r\n            while j > 0:\r\n  \
    \              self.bit[i][j] += val\r\n                j -= j & -j\r\n      \
    \      i -= i & -i\r\n\r\n    def add(self, hl, hr, wl, wr, val):\r\n        \"\
    \"\"add value in range [l, r)\"\"\"\r\n        self._add(hl, wl, val)\r\n    \
    \    self._add(hr, wl, -val)\r\n        self._add(hl, wr, -val)\r\n        self._add(hr,\
    \ wr, val)\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\BinaryIndexedTree\RangeAddPointGet2D.py
  requiredBy: []
  timestamp: '2021-01-02 15:42:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_5_B.BIT.test.py
documentation_of: DataStructure\BinaryIndexedTree\RangeAddPointGet2D.py
layout: document
title: "\u77E9\u5F62\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
---
