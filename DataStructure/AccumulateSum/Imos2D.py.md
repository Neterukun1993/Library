---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_5_B.test.py
    title: TestCase/AOJ/DSL_5_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Imos2D:\n    def __init__(self, h, w):\n        self.h = h\n      \
    \  self.w = w\n        self.imos = [[0] * (self.w + 1) for _ in range(self.h +\
    \ 1)]\n\n    def __getitem__(self, ij):\n        i, j = ij\n        return self.imos[i][j]\n\
    \n    def add(self, hl, hr, wl, wr, val):\n        \"\"\"add value in range [hl,\
    \ hr) * [wl, wr)\"\"\"\n        self.imos[hl][wl] += val\n        self.imos[hr][wl]\
    \ -= val\n        self.imos[hl][wr] -= val\n        self.imos[hr][wr] += val\n\
    \n    def build(self):\n        for i in range(self.h):\n            for j in\
    \ range(self.w):\n                self.imos[i][j + 1] += self.imos[i][j]\n   \
    \     for i in range(self.h):\n            for j in range(self.w):\n         \
    \       self.imos[i + 1][j] += self.imos[i][j]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/Imos2D.py
  requiredBy: []
  timestamp: '2021-01-02 06:13:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_5_B.test.py
documentation_of: DataStructure/AccumulateSum/Imos2D.py
layout: document
redirect_from:
- /library/DataStructure/AccumulateSum/Imos2D.py
- /library/DataStructure/AccumulateSum/Imos2D.py.html
title: DataStructure/AccumulateSum/Imos2D.py
---
