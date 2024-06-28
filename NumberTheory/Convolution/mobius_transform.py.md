---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/and_convolve.py
    title: "\u6DFB\u5B57 and \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/or_convolve.py
    title: "\u6DFB\u5B57 or \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/zeta_mobius_transform.unittest.test.py
    title: TestCase/unittest/zeta_mobius_transform.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def subset_mobius_transform(a, op, inv):\n    n = len(a)\n    res = a[:]\n\
    \    for k in range((n - 1).bit_length()):\n        bit = 1 << k\n        for\
    \ i in range(n):\n            if i & bit:\n                res[i] = op(inv(res[i\
    \ & ~bit]), res[i])\n    return res\n\n\ndef superset_mobius_transform(a, op,\
    \ inv):\n    n = len(a)\n    res = a[:]\n    for k in range((n - 1).bit_length()):\n\
    \        bit = 1 << k\n        for i in range(n):\n            if i & bit:\n \
    \               res[i & ~bit] = op(res[i & ~bit], inv(res[i]))\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/mobius_transform.py
  requiredBy:
  - NumberTheory/Convolution/and_convolve.py
  - NumberTheory/Convolution/or_convolve.py
  timestamp: '2021-06-20 22:49:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/zeta_mobius_transform.unittest.test.py
documentation_of: NumberTheory/Convolution/mobius_transform.py
layout: document
title: "\u9AD8\u901F\u30E1\u30D3\u30A6\u30B9\u5909\u63DB (fast m\xF6bius transform)"
---
