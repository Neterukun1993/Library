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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def primitive_root(p):\n    if p == 2:\n        return 1\n    x = p - 1\n\
    \    factors = [2]\n    while x % 2 == 0:\n        x //= 2\n    for k in range(3,\
    \ int(p ** 0.5) + 1, 2):\n        if x % k == 0:\n            factors.append(k)\n\
    \            while x % k == 0:\n                x //= k\n    if x != 1:\n    \
    \    factors.append(x)\n\n    g = 2\n    while True:\n        ok = True\n    \
    \    for val in factors:\n            if pow(g, (p - 1) // val, p) == 1:\n   \
    \             ok = False\n                break\n        if ok:\n            return\
    \ g\n        g += 1\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/primitive_root.py
  requiredBy: []
  timestamp: '2021-09-25 04:04:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/ModularArithmetic/primitive_root.py
layout: document
title: "\u539F\u59CB\u6839"
---

## 概要
素数 $p$ の最小の原始根を求めるアルゴリズム。

## 使い方
`primitive_root(p: int) -> int`  
素数 $p$ の最小の原始根を求める。
