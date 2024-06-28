---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/sum_of_totient_function.test.py
    title: TestCase/LibraryChecker/sum_of_totient_function.test.py
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
  code: "import math\n\n\ndef totient_sum(n, MOD):\n    assert(n > 0)\n    if n ==\
    \ 1: return 1\n    if n == 2: return 2\n\n    k = int((n / math.log2(math.log2(n)))\
    \ ** (2 / 3)) + 1\n    phi = [i for i in range(k)]\n\n    for i in range(2, k):\n\
    \        if phi[i] == i:\n            for j in range(i, k, i):\n             \
    \   phi[j] -= phi[j] // i\n                phi[j] %= MOD\n    for i in range(k\
    \ - 1):\n        phi[i + 1] += phi[i]\n        phi[i + 1] %= MOD\n\n    phi2 =\
    \ [0] * ((n + k - 2) // (k - 1))\n    for i in range(1, len(phi2)):\n        phi2[i]\
    \ = (n // i) * (n // i + 1) // 2 % MOD\n\n    for i in reversed(range(1, len(phi2))):\n\
    \        cur = n // i\n        j = 2\n        while cur // j != cur // (j + 1)\
    \ and j <= cur:\n            if i * j >= len(phi2):\n                phi2[i] -=\
    \ phi[cur // j]\n            else:\n                phi2[i] -= phi2[i * j]\n \
    \           phi2[i] %= MOD\n            j += 1\n        for arg in reversed(range(1,\
    \ cur // j + 1)):\n            if arg < k:\n                phi2[i] -= (cur //\
    \ arg - cur // (arg + 1)) * phi[arg]\n            else:\n                phi2[i]\
    \ -= (cur // arg - cur // (arg + 1)) * phi2[n // arg]\n            phi2[i] %=\
    \ MOD\n\n    return phi2[1]\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/misc/totient_sum.py
  requiredBy: []
  timestamp: '2022-08-07 16:49:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/sum_of_totient_function.test.py
documentation_of: NumberTheory/misc/totient_sum.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u306E $\\varphi$ \u95A2\u6570\u306E\u548C"
---

## 使い方
`totient_sum(n: int, MOD: int) -> int`  
$\sum_{i=1}^{n}{\varphi(i)}$ を $\mathrm{MOD}$ で割ったあまりを返す。計算量 $O(N^{2/3}(\log\log{N})^{1/3})$

## 参考
[トーティエント関数 $\varphi(i)$ の和 $\sum_{i=1}^{N}{\varphi(i)}$ を $O(N^{2/3}(\log\log{N})^{1/3})$ で求める Wiki - yukicoder](https://yukicoder.me/wiki/sum_totient)