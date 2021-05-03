---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0206.test.py
    title: TestCase/yukicoder/yuki0206.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from cmath import pi, exp\n\n\ndef _fft(a, h):\n    roots = [exp(2.0j * pi\
    \ / 2 ** i) for i in range(h + 1)]\n    for i in range(h):\n        m = 1 << (h\
    \ - i - 1)\n        for j in range(1 << i):\n            w = 1\n            j\
    \ *= 2 * m\n            for k in range(m):\n                a[j + k], a[j + k\
    \ + m] = \\\n                    a[j + k] + a[j + k + m], (a[j + k] - a[j + k\
    \ + m]) * w\n                w *= roots[h - i]\n\n\ndef _ifft(a, h):\n    iroots\
    \ = [exp(-2.0j * pi / 2 ** i) for i in range(h + 1)]\n    for i in range(h):\n\
    \        m = 1 << i\n        for j in range(1 << (h - i - 1)):\n            w\
    \ = 1\n            j *= 2 * m\n            for k in range(m):\n              \
    \  a[j + k], a[j + k + m] = \\\n                    a[j + k] + a[j + k + m] *\
    \ w, a[j + k] - a[j + k + m] * w\n                w *= iroots[i + 1]\n    n =\
    \ 1 << h\n    for i in range(n):\n        a[i] /= n\n\n\ndef fft_convolve(a, b):\n\
    \    n = 1 << (len(a) + len(b) - 1).bit_length()\n    h = n.bit_length() - 1\n\
    \    a = list(a) + [0] * (n - len(a))\n    b = list(b) + [0] * (n - len(b))\n\n\
    \    _fft(a, h), _fft(b, h)\n    a = [va * vb for va, vb in zip(a, b)]\n    _ifft(a,\
    \ h)\n    return [int(abs(val) + 0.5) for val in a]\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/fft_convolve.py
  requiredBy: []
  timestamp: '2021-05-03 11:23:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0206.test.py
documentation_of: NumberTheory/Convolution/fft_convolve.py
layout: document
title: "\u9AD8\u901F\u30D5\u30FC\u30EA\u30A8\u5909\u63DB (fast Fourier transform)"
---
