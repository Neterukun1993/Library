---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\static_range_sum.test.py
    title: TestCase\LibraryChecker\static_range_sum.test.py
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
  code: "class AccumulateSum:\r\n    def __init__(self, array):\r\n        self.n\
    \ = len(array)\r\n        self.cumsum = [0] * (self.n + 1)\r\n        for i, val\
    \ in enumerate(array):\r\n            self.cumsum[i + 1] = self.cumsum[i] + val\r\
    \n\r\n    def sum(self, l, r):\r\n        return self.cumsum[r] - self.cumsum[l]\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\AccumulateSum\AccumulateSum.py
  requiredBy: []
  timestamp: '2021-01-01 19:51:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\static_range_sum.test.py
documentation_of: DataStructure\AccumulateSum\AccumulateSum.py
layout: document
title: "\u7D2F\u7A4D\u548C"
---
## 使い方
`AccumulateSum(array: List[Any])`  
`array` の累積和を構築する。計算量 $\mathrm{O}(\mathrm{len}(array))$
- `sum(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $\mathrm{O}(1)$
