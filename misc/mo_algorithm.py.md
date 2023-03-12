---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AtCoder/abc242_g.test.py
    title: TestCase/AtCoder/abc242_g.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "SIZE = 256\n\n\ndef mo_algorithm(n, q, intervals, add1, add2, rem1, rem2,\
    \ get):\n    orders = [((l // SIZE) << 40) + (r << 20) + i for i, (l, r) in enumerate(intervals)]\n\
    \    orders.sort()\n    answers = [0] * q\n    nl, nr = 0, 0\n\n    for order\
    \ in orders:\n        i = order & ((1 << 20) - 1)\n        l, r = intervals[i]\n\
    \        while nl > l:\n            nl -= 1\n            add1(nl)\n        while\
    \ nr < r:\n            add2(nr)\n            nr += 1\n        while nl < l:\n\
    \            rem1(nl)\n            nl += 1\n        while nr > r:\n          \
    \  nr -= 1\n            rem2(nr)\n        answers[i] = get()\n    return answers\n"
  dependsOn: []
  isVerificationFile: false
  path: misc/mo_algorithm.py
  requiredBy: []
  timestamp: '2023-03-12 18:21:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AtCoder/abc242_g.test.py
documentation_of: misc/mo_algorithm.py
layout: document
redirect_from:
- /library/misc/mo_algorithm.py
- /library/misc/mo_algorithm.py.html
title: misc/mo_algorithm.py
---
