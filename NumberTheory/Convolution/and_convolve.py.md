---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/mobius_transform.py
    title: "\u9AD8\u901F\u30E1\u30D3\u30A6\u30B9\u5909\u63DB (fast m\xF6bius transform)"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/zeta_transform.py
    title: "\u9AD8\u901F\u30BC\u30FC\u30BF\u5909\u63DB (fast zeta transform)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/bitwise_and_convolution.and.test.py
    title: TestCase/LibraryChecker/bitwise_and_convolution.and.test.py
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
  code: "from NumberTheory.Convolution.zeta_transform import superset_zeta_transform\n\
    from NumberTheory.Convolution.mobius_transform import superset_mobius_transform\n\
    MOD = 998244353\n\n\ndef and_convolve(a, b):\n    add = lambda x, y: (x + y) %\
    \ MOD\n    inv = lambda x: -x\n    mul = lambda x, y: (x * y) % MOD\n\n    a =\
    \ superset_zeta_transform(a, add)\n    b = superset_zeta_transform(b, add)\n \
    \   res = [mul(v1, v2) for v1, v2 in zip(a, b)]\n    res = superset_mobius_transform(res,\
    \ add, inv)\n    return res\n"
  dependsOn:
  - NumberTheory/Convolution/mobius_transform.py
  - NumberTheory/Convolution/zeta_transform.py
  isVerificationFile: false
  path: NumberTheory/Convolution/and_convolve.py
  requiredBy: []
  timestamp: '2021-06-21 01:35:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/bitwise_and_convolution.and.test.py
documentation_of: NumberTheory/Convolution/and_convolve.py
layout: document
title: "\u6DFB\u5B57 and \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
---
