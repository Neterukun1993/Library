---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0225.test.py
    title: TestCase/yukicoder/yuki0225.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def levenshtein_distance(s, t):\n    len_s = len(s)\n    len_t = len(t)\n\
    \    INF = 10 ** 18\n    dp = [[INF] * (len_t + 1) for _ in range(len_s + 1)]\n\
    \    for i in range(len_s + 1):\n        dp[i][0] = i\n    for j in range(len_t\
    \ + 1):\n        dp[0][j] = j\n\n    for i in range(len_s):\n        for j in\
    \ range(len_t):\n            # \u5909\u66F4\u64CD\u4F5C\n            if s[i] ==\
    \ t[j]:\n                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])\n\
    \            else:\n                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j]\
    \ + 1)\n            # \u524A\u9664\u64CD\u4F5C\n            dp[i + 1][j + 1] =\
    \ min(dp[i + 1][j + 1], dp[i][j + 1] + 1)\n            # \u633F\u5165\u64CD\u4F5C\
    \n            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + 1)\n\n \
    \   return dp[len_s][len_t]\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/levenshtein_distance.py
  requiredBy: []
  timestamp: '2021-05-05 22:42:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0225.test.py
documentation_of: DP/levenshtein_distance.py
layout: document
title: "\u7DE8\u96C6\u8DDD\u96E2 (\u30EC\u30FC\u30D9\u30F3\u30B7\u30E5\u30BF\u30A4\
  \u30F3\u8DDD\u96E2)"
---

## 概要
文字列 $S$ を $T$ へと変換するときの最小の操作回数を求めるアルゴリズム。操作には以下の方法がある。
 - 変更操作: $S$ から文字を $1$ 個選び、変更する。
 - 削除操作: $S$ から文字を $1$ 個選び、削除する。 
 - 挿入操作: $S$ の好きな箇所に文字を $1$ 個挿入する。

## 使い方
`levenshtein_distance(s: str, t: str) -> int`  
長さ $N$ の文字列 `s` を 長さ $M$ の文字列 `t` に変換するときの最小操作回数を返す。計算量 $O(NM)$
