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
  code: "def MP(string):\n    border = [0] * (len(string) + 1)\n    border[0] = -1\n\
    \    j = -1\n    for i in range(len(a)):\n        while j >= 0 and string[i] !=\
    \ string[j]):\n            j = border[j]\n    j += 1\n    border[i + 1] = j\n\
    \    return border\n"
  dependsOn: []
  isVerificationFile: false
  path: String/MP.py
  requiredBy: []
  timestamp: '2021-01-25 20:12:07+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/MP.py
layout: document
redirect_from:
- /library/String/MP.py
- /library/String/MP.py.html
title: String/MP.py
---
