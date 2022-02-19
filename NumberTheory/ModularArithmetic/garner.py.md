---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/extended_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0187.test.py
    title: TestCase/yukicoder/yuki0187.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from NumberTheory.Basic.extended_gcd import extended_gcd, mod_inv\n\n\ndef\
    \ pregarner(a, m, MOD):\n    def gcd(a, b):\n        while b:\n            a,\
    \ b = b, a % b\n        return a\n    a, m = a[:], m[:]\n    n = len(a)\n    for\
    \ i in range(n):\n        for j in range(i):\n            g = gcd(m[i], m[j])\n\
    \            if (a[i] - a[j]) % g != 0:\n                return -1, a, m\n   \
    \         m[i], m[j] = m[i] // g, m[j] // g\n            gi = gcd(m[i], g)\n \
    \           gj = g // gi\n            while True:\n                g = gcd(gi,\
    \ gj)\n                gi, gj = gi * g, gj // g\n                if g == 1:\n\
    \                    break\n            m[i], m[j] = m[i] * gi, m[j] * gj\n  \
    \          a[i], a[j] = a[i] % m[i], a[j] % m[j]\n    lcm = 1\n    for i in range(n):\n\
    \        lcm = lcm * m[i] % MOD\n    return lcm, a, m\n\n\ndef garner(a, m, MOD):\n\
    \    n = len(m)\n    m = m + [MOD]\n    coeff = [1] * (n + 1)\n    res = [0] *\
    \ (n + 1)\n    for i in range(n):\n        t = (a[i] - res[i]) * mod_inv(coeff[i],\
    \ m[i]) % m[i]\n        for j in range(i + 1, n + 1):\n            res[j] = (res[j]\
    \ + t * coeff[j]) % m[j]\n            coeff[j] = coeff[j] * m[i] % m[j]\n    return\
    \ res[-1]\n"
  dependsOn:
  - NumberTheory/Basic/extended_gcd.py
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/garner.py
  requiredBy: []
  timestamp: '2021-05-03 15:04:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0187.test.py
documentation_of: NumberTheory/ModularArithmetic/garner.py
layout: document
title: "Garner \u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0"
---

## 概要
$m_0, m_1, \cdots, m_{n - 1}$ と $a_0, a_1, \cdots, a_{n - 1}$ について

$$\left\{\begin{array}{l}x \equiv a_0 \pmod{m_0}\\x \equiv a_1 \pmod{m_1}\\ \cdots \\x \equiv a_{n - 1} \pmod{m_{n - 1}}\end{array}\right.$$

を満たす $x$ を求めるアルゴリズム。

## 使い方
`pregarner(a: Sequence[int], m: Sequence[int], MOD: int) -> Tuple[int, Sequence[int], Sequence[int]]`  
互いに素でない $m_i, m_j (i \ne j)$ があるときに Garner のアルゴリズムを適応するための前処理
を行う。
- $1$ 番目の返り値が $-1$ のとき、$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす $x$ は存在しない。このときの $2, 3$ 番目の返り値は未定義。
- $1$ 番目の返り値が $-1$ でないとき、$1$ 番目の返り値は $\mathrm{MOD}$ 上の $\mathrm{lcm}(m[i])$ である。$2, 3$ 番目の返り値は前処理された $a$ と $m$ である。

`pregarner(a: Sequence[int], m: Sequence[int], MOD: int) -> Tuple[int, Sequence[int], Sequence[int]]`  
$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす最小の非負整数 $x$ を $\mathrm{MOD}$ で割った余りを返す。そのような $x$ が存在しない場合は $-1$ を返す。計算量 $O(N^2)$
