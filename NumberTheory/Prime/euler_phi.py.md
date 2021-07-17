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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def euler_phi(n):\n    ans = n\n    for i in range(2, int(n ** 0.5) + 1):\n\
    \        if n % i == 0:\n            while n % i == 0:\n                n //=\
    \ i\n            ans -= ans // i\n    if n > 1:\n        ans -= ans // n\n   \
    \ return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/euler_phi.py
  requiredBy: []
  timestamp: '2021-06-19 23:52:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/Prime/euler_phi.py
layout: document
redirect_from:
- /library/NumberTheory/Prime/euler_phi.py
- /library/NumberTheory/Prime/euler_phi.py.html
title: NumberTheory/Prime/euler_phi.py
---
