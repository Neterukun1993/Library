---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_10_C.test.py
    title: TestCase/AOJ/ALDS1_10_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def lcs(s, t):\n    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]\n\
    \    for i, chr_s in enumerate(s):\n        for j, chr_t in enumerate(t):\n  \
    \          if chr_s == chr_t:\n                dp[i + 1][j + 1] = dp[i][j] + 1\n\
    \            else:\n                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i\
    \ + 1][j])\n\n    res = []\n    i, j = len(s), len(t)\n    while i > 0 and j >\
    \ 0:\n        if dp[i][j] == dp[i - 1][j]:\n            i -= 1\n        elif dp[i][j]\
    \ == dp[i][j - 1]:\n            j -= 1\n        else:\n            res.append(s[i\
    \ - 1])\n            i -= 1\n            j -= 1\n    return ''.join(reversed(res))\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/lcs.py
  requiredBy: []
  timestamp: '2021-05-06 21:57:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_10_C.test.py
documentation_of: DP/lcs.py
layout: document
title: "\u6700\u9577\u5171\u901A\u90E8\u5206\u5217 (longest common subsequence)"
---

## 概要
最長共通部分列を求めるアルゴリズム。

## 使い方
`lcs(s: str, t: str) -> str`  
長さ $N$ の文字列 `s` と長さ $M$ の文字列 `t` の最長共通部分列を返す。計算量 $O(NM)$
