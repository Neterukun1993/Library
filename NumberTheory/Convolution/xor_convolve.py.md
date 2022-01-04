---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/bitwise_xor_convolution.test.py
    title: TestCase/LibraryChecker/bitwise_xor_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef _wht(a, h):\n    for k in range(h):\n        bit\
    \ = 1 << k\n        for i in range(1 << h):\n            if i & bit == 0:\n  \
    \              x, y = a[i], a[i | bit]\n                a[i] = (x + y) % MOD\n\
    \                a[i | bit] = (x - y) % MOD\n\n\ndef _iwht(a, h):\n    _wht(a,\
    \ h)\n    invn = pow(1 << h, MOD - 2, MOD)\n    for i in range(1 << h):\n    \
    \    a[i] *= invn\n        a[i] %= MOD\n\n\ndef xor_convolve(a, b):\n    n = 1\
    \ << (max(len(a), len(b)) - 1).bit_length()\n    h = n.bit_length() - 1\n    a\
    \ = list(a) + [0] * (n - len(a))\n    b = list(b) + [0] * (n - len(b))\n\n   \
    \ _wht(a, h), _wht(b, h)\n    a = [(va * vb) % MOD for va, vb in zip(a, b)]\n\
    \    _iwht(a, h)\n    return a\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/xor_convolve.py
  requiredBy: []
  timestamp: '2021-06-21 01:35:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/bitwise_xor_convolution.test.py
documentation_of: NumberTheory/Convolution/xor_convolve.py
layout: document
title: "\u6DFB\u5B57 xor \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
---
