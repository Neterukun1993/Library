---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
    title: TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def eratosthenes_sieve(n):\n    is_prime_tbl = [True] * (n + 1)\n    is_prime_tbl[0]\
    \ = False\n    is_prime_tbl[1] = False\n    for i in range(2, int(n ** 0.5) +\
    \ 1):\n        if not is_prime_tbl[i]:\n            continue\n        for j in\
    \ range(2 * i, n + 1, i):\n            is_prime_tbl[j] = False\n    prime_list\
    \ = [i for i, flag in enumerate(is_prime_tbl) if flag]\n    return prime_list,\
    \ is_prime_tbl\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/eratosthenes_sieve.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
documentation_of: NumberTheory/Prime/eratosthenes_sieve.py
layout: document
title: "\u7D20\u6570\u5217\u6319 (\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\
  \u7BE9)"
---

## 概要
$O(n\log \log n)$ で素数列挙を行うアルゴリズム。

## 使い方
`eratosthenes_sieve(n: int) -> Tuple[List[int], List[int]]`  
`n` 以下の素数のリストと、素数かどうかの判定テーブルを返す。計算量 $O(n \log \log n)$
