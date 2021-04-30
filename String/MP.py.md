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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def MP(s):\n    border = [0] * (len(s) + 1)\n    border[0] = -1\n    j =\
    \ -1\n    for i in range(len(s)):\n        while j >= 0 and s[i] != s[j]:\n  \
    \          j = border[j]\n        j += 1\n        border[i + 1] = j\n    period\
    \ = [i - val for i, val in enumerate(border)]\n    period[0] = -1\n    return\
    \ border, period\n"
  dependsOn: []
  isVerificationFile: false
  path: String/MP.py
  requiredBy: []
  timestamp: '2021-02-12 11:49:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/MP.py
layout: document
title: "MP\u6CD5 (Morrison-Pratt\u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0)"
---
## 使い方
`MP(s: Sequence[Any]) -> Tuple(List[int], List[int])`  
`s[:i]` の最長の境界 (Longest Border) と最短の周期 (Shortest Period) の配列を返す。`n = len(s) + 1` とすると、計算量 $O(n)$
