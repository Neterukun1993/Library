---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/segment_sieve.unittest.test.py
    title: TestCase/unittest/segment_sieve.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def segment_sieve(l, r):\n    sqrt_r = int(r ** 0.5)\n    is_prime_sqrt =\
    \ [True] * (sqrt_r + 1)\n    is_prime_sqrt[0] = False\n    is_prime_sqrt[1] =\
    \ False\n    is_prime_tbl = [True] * (r - l)\n    if l == 0:\n        is_prime_tbl[0]\
    \ = False\n        is_prime_tbl[1] = False\n    if l == 1:\n        is_prime_tbl[0]\
    \ = False\n\n    for i in range(2, sqrt_r + 1):\n        if not is_prime_sqrt[i]:\n\
    \            continue\n        for j in range(2 * i, sqrt_r + 1, i):\n       \
    \     is_prime_sqrt[j] = False\n        for j in range(max((l + i - 1) // i, 2)\
    \ * i, r, i):\n            is_prime_tbl[j - l] = False\n\n    prime_list = [l\
    \ + i for i, flag in enumerate(is_prime_tbl) if flag]\n    return prime_list,\
    \ is_prime_tbl\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/segment_sieve.py
  requiredBy: []
  timestamp: '2021-03-05 16:39:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/segment_sieve.unittest.test.py
documentation_of: NumberTheory/Prime/segment_sieve.py
layout: document
title: "\u7D20\u6570\u5217\u6319 (\u533A\u9593\u7BE9)"
---

## 概要
区間範囲に対して素数列挙を行うアルゴリズム。区間 $[l, r)$ についての制約が

* $1 \le l  \lt r \le 10^9$
* $r − l \le 10^6$

のようなときに使用可能。

## 使い方
`segment_sieve(l: int, r: int) -> Tuple[List[int], List[int]]`  
`l` 以上 `r` 未満の整数について、素数のリストと素数かどうかの判定テーブルを返す。計算量 $O(\sqrt r + (r - l)\log\log r)$
