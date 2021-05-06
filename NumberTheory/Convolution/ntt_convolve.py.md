---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/convolution_mod.test.py
    title: TestCase/LibraryChecker/convolution_mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\nROOT = 5\n\n\ndef _ntt(a, h):\n    roots = [pow(ROOT, (MOD\
    \ - 1) >> i, MOD) for i in range(h + 1)]\n    for i in range(h):\n        m =\
    \ 1 << (h - i - 1)\n        for j in range(1 << i):\n            w = 1\n     \
    \       j *= 2 * m\n            for k in range(m):\n                a[j + k],\
    \ a[j + k + m] = \\\n                    (a[j + k] + a[j + k + m]) % MOD, \\\n\
    \                    (a[j + k] - a[j + k + m]) * w % MOD\n                w *=\
    \ roots[h - i]\n                w %= MOD\n\n\ndef _intt(a, h):\n    roots = [pow(ROOT,\
    \ (MOD - 1) >> i, MOD) for i in range(h + 1)]\n    iroots = [pow(r, MOD - 2, MOD)\
    \ for r in roots]\n    for i in range(h):\n        m = 1 << i\n        for j in\
    \ range(1 << (h - i - 1)):\n            w = 1\n            j *= 2 * m\n      \
    \      for k in range(m):\n                a[j + k], a[j + k + m] = \\\n     \
    \               (a[j + k] + a[j + k + m] * w) % MOD, \\\n                    (a[j\
    \ + k] - a[j + k + m] * w) % MOD\n                w *= iroots[i + 1]\n       \
    \         w %= MOD\n    inv = pow(1 << h, MOD - 2, MOD)\n    for i in range(1\
    \ << h):\n        a[i] *= inv\n        a[i] %= MOD\n\n\ndef ntt_convolve(a, b):\n\
    \    n = 1 << (len(a) + len(b) - 1).bit_length()\n    h = n.bit_length() - 1\n\
    \    a = list(a) + [0] * (n - len(a))\n    b = list(b) + [0] * (n - len(b))\n\n\
    \    _ntt(a, h), _ntt(b, h)\n    a = [va * vb % MOD for va, vb in zip(a, b)]\n\
    \    _intt(a, h)\n    return a\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/ntt_convolve.py
  requiredBy: []
  timestamp: '2021-05-03 11:23:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/convolution_mod.test.py
documentation_of: NumberTheory/Convolution/ntt_convolve.py
layout: document
title: "\u6570\u8AD6\u5909\u63DB (number-theoretic transform)"
---