---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/static_range_sum.test.py
    title: TestCase/LibraryChecker/static_range_sum.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class AccumulateSum:\n    def __init__(self, array):\n        self.n = len(array)\n\
    \        self.cumsum = [0] * (self.n + 1)\n        for i, val in enumerate(array):\n\
    \            self.cumsum[i + 1] = self.cumsum[i] + val\n\n    def sum(self, l,\
    \ r):\n        return self.cumsum[r] - self.cumsum[l]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/AccumulateSum.py
  requiredBy: []
  timestamp: '2021-01-01 19:51:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/static_range_sum.test.py
documentation_of: DataStructure/AccumulateSum/AccumulateSum.py
layout: document
redirect_from:
- /library/DataStructure/AccumulateSum/AccumulateSum.py
- /library/DataStructure/AccumulateSum/AccumulateSum.py.html
title: DataStructure/AccumulateSum/AccumulateSum.py
---
