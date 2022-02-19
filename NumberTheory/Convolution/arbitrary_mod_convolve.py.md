---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
    title: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "M1, R1 = 167772161, 3\nM2, R2 = 469762049, 3\nM3, R3 = 1224736769, 3\n\n\n\
    def MOD1(): return M1\ndef ROOT1(): return R1\ndef MOD2(): return M2\ndef ROOT2():\
    \ return R2\ndef MOD3(): return M3\ndef ROOT3(): return R3\n\n\ndef _ntt(a, h,\
    \ MOD, ROOT):\n    roots = [pow(ROOT(), (MOD() - 1) >> i, MOD()) for i in range(h\
    \ + 1)]\n    for i in range(h):\n        m = 1 << (h - i - 1)\n        for j in\
    \ range(1 << i):\n            w = 1\n            j *= 2 * m\n            for k\
    \ in range(m):\n                a[j + k], a[j + k + m] = \\\n                \
    \    (a[j + k] + a[j + k + m]) % MOD(), \\\n                    (a[j + k] - a[j\
    \ + k + m]) * w % MOD()\n                w *= roots[h - i]\n                w\
    \ %= MOD()\n\n\ndef _intt(a, h, MOD, ROOT):\n    roots = [pow(ROOT(), (MOD() -\
    \ 1) >> i, MOD()) for i in range(h + 1)]\n    iroots = [pow(r, MOD() - 2, MOD())\
    \ for r in roots]\n    for i in range(h):\n        m = 1 << i\n        for j in\
    \ range(1 << (h - i - 1)):\n            w = 1\n            j *= 2 * m\n      \
    \      for k in range(m):\n                a[j + k], a[j + k + m] = \\\n     \
    \               (a[j + k] + a[j + k + m] * w) % MOD(), \\\n                  \
    \  (a[j + k] - a[j + k + m] * w) % MOD()\n                w *= iroots[i + 1]\n\
    \                w %= MOD()\n    inv = pow(1 << h, MOD() - 2, MOD())\n    for\
    \ i in range(1 << h):\n        a[i] *= inv\n        a[i] %= MOD()\n\n\ndef _ntt_convolve(a,\
    \ b, MOD, ROOT):\n    n = 1 << (len(a) + len(b) - 1).bit_length()\n    h = n.bit_length()\
    \ - 1\n    a = list(a) + [0] * (n - len(a))\n    b = list(b) + [0] * (n - len(b))\n\
    \n    _ntt(a, h, MOD, ROOT), _ntt(b, h, MOD, ROOT)\n    a = [va * vb % MOD() for\
    \ va, vb in zip(a, b)]\n    _intt(a, h, MOD, ROOT)\n    return a\n\n\ndef arbitrary_mod_convolve(a,\
    \ b, p):\n    x = _ntt_convolve(a, b, MOD1, ROOT1)\n    y = _ntt_convolve(a, b,\
    \ MOD2, ROOT2)\n    z = _ntt_convolve(a, b, MOD3, ROOT3)\n    mod = p\n\n    inv1_2\
    \ = pow(MOD1(), MOD2() - 2, MOD2())\n    inv12_3 = pow(MOD1() * MOD2(), MOD3()\
    \ - 2, MOD3())\n    mod12 = MOD1() * MOD2() % mod\n\n    res = [0] * (len(a) +\
    \ len(b) - 1)\n    for i in range(len(res)):\n        v1 = (y[i] - x[i]) * inv1_2\
    \ % MOD2()\n        v2 = (z[i] - (x[i] + MOD1() * v1) % MOD3()) * inv12_3 % MOD3()\n\
    \        res[i] = (x[i] + MOD1() * v1 + mod12 * v2) % mod\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Convolution/arbitrary_mod_convolve.py
  requiredBy: []
  timestamp: '2021-06-13 01:12:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
documentation_of: NumberTheory/Convolution/arbitrary_mod_convolve.py
layout: document
title: "\u4EFB\u610F MOD \u7573\u307F\u8FBC\u307F"
---

## 使い方
`arbitrary_mod_convolve(a: Sequence[int], b: Sequence[int], p: int) -> List[int]`  
長さ $N$ の数列 $a$ と長さ $M$ の数列 $b$ について、$c_k = \sum_{i + j \equiv k} a_ib_j \bmod p$ となる長さ $N + M - 1$ の数列 $c$ を返す。計算量 $O((N + M) \log (N + M))$
