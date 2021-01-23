---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_5_B.test.py
    title: TestCase\AOJ\DSL_5_B.test.py
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
  code: "class Imos2D:\r\n    def __init__(self, h, w):\r\n        self.h = h\r\n\
    \        self.w = w\r\n        self.imos = [[0] * (self.w + 1) for _ in range(self.h\
    \ + 1)]\r\n\r\n    def __getitem__(self, ij):\r\n        i, j = ij\r\n       \
    \ return self.imos[i][j]\r\n\r\n    def add(self, hl, hr, wl, wr, val):\r\n  \
    \      \"\"\"add value in range [hl, hr) * [wl, wr)\"\"\"\r\n        self.imos[hl][wl]\
    \ += val\r\n        self.imos[hr][wl] -= val\r\n        self.imos[hl][wr] -= val\r\
    \n        self.imos[hr][wr] += val\r\n\r\n    def build(self):\r\n        for\
    \ i in range(self.h):\r\n            for j in range(self.w):\r\n             \
    \   self.imos[i][j + 1] += self.imos[i][j]\r\n        for i in range(self.h):\r\
    \n            for j in range(self.w):\r\n                self.imos[i + 1][j] +=\
    \ self.imos[i][j]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\AccumulateSum\Imos2D.py
  requiredBy: []
  timestamp: '2021-01-02 06:13:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_5_B.test.py
documentation_of: DataStructure\AccumulateSum\Imos2D.py
layout: document
title: "\u4E8C\u6B21\u5143\u3044\u3082\u3059\u6CD5"
---
