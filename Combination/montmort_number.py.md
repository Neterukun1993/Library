---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/montmort_number_mod.test.py
    title: TestCase/LibraryChecker/montmort_number_mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def montmort_number(n, MOD):\n    dp = [0] * (n + 1)\n    if n >= 2:\n  \
    \      dp[2] = 1\n    for i in range(3, n + 1):\n        dp[i] = (i - 1) * (dp[i\
    \ - 1] + dp[i - 2])\n        dp[i] %= MOD\n    return dp\n\n\ndef montmort_number2(n,\
    \ MOD):\n    dp = [0] * (n + 1)\n    for i in range(1, n):\n        dp[i + 1]\
    \ = (i + 1) * dp[i] + (-1) ** ((i + 1) & 1)\n        dp[i + 1] %= MOD\n    return\
    \ dp\n"
  dependsOn: []
  isVerificationFile: false
  path: Combination/montmort_number.py
  requiredBy: []
  timestamp: '2021-01-27 22:05:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/montmort_number_mod.test.py
documentation_of: Combination/montmort_number.py
layout: document
title: "\u30E2\u30F3\u30E2\u30FC\u30EB\u6570 (\u5B8C\u5168\u9806\u5217)"
---
