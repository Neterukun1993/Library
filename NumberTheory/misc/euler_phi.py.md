---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/NTL_1_D.test.py
    title: TestCase/AOJ/NTL_1_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/euler_phi_table.unittest.test.py
    title: TestCase/unittest/euler_phi_table.unittest.test.py
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
  code: "def euler_phi(n):\n    ans = n\n    for i in range(2, int(n ** 0.5) + 1):\n\
    \        if n % i == 0:\n            while n % i == 0:\n                n //=\
    \ i\n            ans -= ans // i\n    if n > 1:\n        ans -= ans // n\n   \
    \ return ans\n\n\ndef euler_phi_table(n):\n    phi = [i for i in range(n + 1)]\n\
    \    for i in range(2, n + 1):\n        if phi[i] == i:\n            for j in\
    \ range(i, n + 1, i):\n                phi[j] -= phi[j] // i\n    return phi\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/misc/euler_phi.py
  requiredBy: []
  timestamp: '2021-08-12 23:00:53+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/euler_phi_table.unittest.test.py
  - TestCase/AOJ/NTL_1_D.test.py
documentation_of: NumberTheory/misc/euler_phi.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u306E $\\varphi$ \u95A2\u6570"
---

## 使い方
`euler_phi(n: int) -> int`  
正の整数 $n$ について、$n$ と互いに素な $n$ 以下の正の整数の個数を返す。計算量 $O(\sqrt{n})$

`euler_phi_table(n: int) -> List[int]`  
$n$ 以下の $\varphi (n)$ をすべて求めたテーブルを返す。計算量 $O(n \log \log n)$
