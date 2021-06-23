---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: NumberTheory/Convolution/gcd_convolve.py
    title: "\u6DFB\u5B57 gcd \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/multiple_divisor_transform.unittest.test.py
    title: TestCase/unittest/multiple_divisor_transform.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def multiple_zeta_transform(a, op):\n    n = len(a)\n    res = a[:]\n   \
    \ prime_table = [1] * n\n    for p in range(2, n):\n        if not prime_table[p]:\n\
    \            continue\n        i = (n - 1) // p\n        while i > 0:\n      \
    \      res[i] = op(res[i], res[i * p])\n            prime_table[i * p] = 0\n \
    \           i -= 1\n    return res\n\n\ndef multiple_mobius_transform(a, op, inv):\n\
    \    n = len(a)\n    res = a[:]\n    prime_table = [1] * n\n    for p in range(2,\
    \ n):\n        if not prime_table[p]:\n            continue\n        i = 1\n \
    \       while i * p < n:\n            res[i] = op(res[i], inv(res[i * p]))\n \
    \           prime_table[i * p] = 0\n            i += 1\n    return res\n\n\ndef\
    \ divisor_zeta_transform(a, op):\n    n = len(a)\n    res = a[:]\n    prime_table\
    \ = [1] * n\n    for p in range(2, n):\n        if not prime_table[p]:\n     \
    \       continue\n        i = 1\n        while i * p < n:\n            res[i *\
    \ p] = op(res[i], res[i * p])\n            prime_table[i * p] = 0\n          \
    \  i += 1\n    return res\n\n\ndef divisor_mobius_transform(a, op, inv):\n   \
    \ n = len(a)\n    res = a[:]\n    prime_table = [1] * n\n    for p in range(2,\
    \ n):\n        if not prime_table[p]:\n            continue\n        i = (n -\
    \ 1) // p\n        while i > 0:\n            res[i * p] = op(inv(res[i]), res[i\
    \ * p])\n            prime_table[i * p] = 0\n            i -= 1\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/multiple_divisor_transform.py
  requiredBy:
  - NumberTheory/Convolution/gcd_convolve.py
  timestamp: '2021-06-21 06:14:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/multiple_divisor_transform.unittest.test.py
documentation_of: NumberTheory/Convolution/multiple_divisor_transform.py
layout: document
title: "\u7D04\u6570/\u500D\u6570\u3092\u96C6\u5408\u3068\u3057\u305F\u7D2F\u7A4D\u548C\
  /\u5DEE\u5206"
---
