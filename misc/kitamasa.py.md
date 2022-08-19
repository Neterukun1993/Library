---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 10 ** 9 + 7\nadd = lambda a, b: (a + b) % MOD\ne_add = lambda: 0\n\
    mul = lambda a, b: a * b % MOD\n# e_mul = lambda: 1\n\n\ndef kitamasa(a, d, n):\n\
    \    # n is 0-indexed\n    def increment(cs):\n        res = [e_add() for _ in\
    \ range(k)]\n        res[0] = mul(d[0], cs[-1])\n        for i in range(1, k):\n\
    \            res[i] = add(cs[i - 1], mul(d[i], cs[-1]))\n        return res\n\n\
    \    def double(cs):\n        mat = []\n        mat.append(cs)\n        for i\
    \ in range(k - 1):\n            mat.append(increment(mat[-1]))\n        res =\
    \ [e_add() for _ in range(k)]\n        for i in range(k):\n            for j in\
    \ range(k):\n                res[j] = add(res[j], mul(mat[i][j], cs[i]))\n   \
    \     return res\n\n    def dfs(cs, n):\n        if n == k:\n            return\
    \ d\n        if (n & 1 or n < k * 2):\n            cs = dfs(cs, n - 1)\n     \
    \       res = increment(cs)\n        else:\n            cs = dfs(cs, n // 2)\n\
    \            res = double(cs)\n        return res\n\n    k = len(d)\n    if k\
    \ > n:\n        return a[n]\n    coeffs = dfs(d, n)\n    ans = e_add()\n    for\
    \ vc, va in zip(coeffs, a):\n        ans = add(ans, mul(vc, va))\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: misc/kitamasa.py
  requiredBy: []
  timestamp: '2021-05-03 19:40:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: misc/kitamasa.py
layout: document
title: "\u304D\u305F\u307E\u3055\u6CD5"
---

## 使い方
`kitamasa(a: Sequence[int], d: Sequence[int], n: int):`  
初めの $k$ 項 $(a_0, a_1, \dots, a_{k-1})$ と係数 $d = (d_0, d_1, \dots, d_{k-1})$ による漸化式

$$a_{n} = d_0 a_{n-k} + d_1 a_{n-k + 1} + \dots + d_{k-1} a_{n-1}$$

で定まる数列の第 $n$ 項 $a_n$ を返す。$n$ は 0-indexed であることに注意。計算量 $O(K^2 \log N)$
