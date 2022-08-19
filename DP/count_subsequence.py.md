---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/number_of_subsequences.test.py
    title: TestCase/LibraryChecker/number_of_subsequences.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def count_subsequence(a, MOD):\n    n = len(a)\n    idx = {}\n    dp = [0]\
    \ * (n + 1)\n    dp[0] = 1\n    for i, val in enumerate(a):\n        if val in\
    \ idx:\n            dp[i + 1] = 2 * dp[i] - dp[idx[val]]\n        else:\n    \
    \        dp[i + 1] = 2 * dp[i]\n        dp[i + 1] %= MOD\n        idx[val] = i\n\
    \    return dp[n]\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/count_subsequence.py
  requiredBy: []
  timestamp: '2022-07-30 20:30:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/number_of_subsequences.test.py
documentation_of: DP/count_subsequence.py
layout: document
title: "\u90E8\u5206\u5217 DP ($O(N)$)"
---
## 概要
数列 $A$ に対して部分列の通り数を求めるアルゴリズム。

## 使い方
- `count_subsequence(a: Sequence, MOD: int) -> int`  
数列 $A$ について、部分列の通り数を $\mathrm{MOD}$ で割った余りを返す。計算量 $O(N)$
