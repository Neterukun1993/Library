---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/multiple_divisor_transform.py
    title: "\u7D04\u6570/\u500D\u6570\u3092\u96C6\u5408\u3068\u3057\u305F\u7D2F\u7A4D\
      \u548C/\u5DEE\u5206"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/lcm_convolution.test.py
    title: TestCase/LibraryChecker/lcm_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from NumberTheory.Convolution.multiple_divisor_transform import (\n    divisor_zeta_transform,\n\
    \    divisor_mobius_transform\n)\nMOD = 998244353\n\n\ndef lcm_convolve(a, b):\n\
    \    add = lambda x, y: (x + y) % MOD\n    inv = lambda x: -x\n    mul = lambda\
    \ x, y: (x * y) % MOD\n\n    a = divisor_zeta_transform(a, add)\n    b = divisor_zeta_transform(b,\
    \ add)\n    res = [mul(v1, v2) for v1, v2 in zip(a, b)]\n    res = divisor_mobius_transform(res,\
    \ add, inv)\n    return res\n"
  dependsOn:
  - NumberTheory/Convolution/multiple_divisor_transform.py
  isVerificationFile: false
  path: NumberTheory/Convolution/lcm_convolve.py
  requiredBy: []
  timestamp: '2022-07-31 17:54:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/lcm_convolution.test.py
documentation_of: NumberTheory/Convolution/lcm_convolve.py
layout: document
title: "\u6DFB\u5B57 lcm \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
---
