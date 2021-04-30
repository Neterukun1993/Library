---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/segment_sieve.unittest.test.py
    title: TestCase/unittest/segment_sieve.unittest.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki3030.test.py
    title: TestCase/yukicoder/yuki3030.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def miller_rabin(n):\n    if n == 2:\n        return True\n    if n == 1\
    \ or n % 2 == 0:\n        return False\n\n    s = 0\n    d = n - 1\n    while\
    \ d & 1 == 0:\n        s += 1\n        d >>= 1\n    for a in (2, 325, 9375, 28178,\
    \ 450775, 9780504, 1795265022):\n        if n <= a:\n            break\n     \
    \   x = pow(a, d, n)\n        if x == 1:\n            continue\n        for _\
    \ in range(s):\n            if x == n - 1:\n                break\n          \
    \  x = x * x % n\n        else:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/miller_rabin.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki3030.test.py
  - TestCase/unittest/segment_sieve.unittest.test.py
documentation_of: NumberTheory/Prime/miller_rabin.py
layout: document
title: "\u78BA\u7387\u7684\u7D20\u6570\u5224\u5B9A (\u30DF\u30E9\u30FC\u30FB\u30E9\
  \u30D3\u30F3\u7D20\u6570\u5224\u5B9A\u6CD5)"
---

## 概要
確率的素数判定を行うアルゴリズム。$n < 2^{64}$ の範囲では決定的に素数判定できるよう実装している。

#### ミラー・ラビン素数判定法の定理
奇素数 $p = 2^s \cdot d + 1$ ($d$ は奇数) に対して、以下のいずれかが任意の整数 $a$ ($0 \lt a \lt p$) について成り立つ。

* $a^d \equiv 1 \pmod{p}$
* $a^{2^r \cdot d} \equiv -1 \pmod{p}$ となる $r$ ($0 \le r \lt s$) が存在


#### ミラー・ラビン素数判定法の定理の対偶
奇数 $n = 2^s \cdot d + 1$ ($d$ は奇数) に対して、以下のすべて満たす整数 $a$ が存在するならば、$n$ は合成数である。

* $a^d \not\equiv 1 \pmod{p}$
* 任意の $r$ ($0 \le r \lt s$)
 について $a^{2^r \cdot d} \not\equiv -1 \pmod{p}$

ミラー・ラビン素数判定法では、この対偶を用いて確率的素数判定を行う。小さい整数の範囲では決定的に素数判定できる。例えば、$a = 2, 325, 9375, 28178, 450775, 9780504, 1795265022$ を用いることで、$n < 2^{64}$ の範囲では決定的になる。

## 使い方
`miller_rabin(n: int) -> bool`  
`n` の確率的素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。`n` が $2^{64}$ までの範囲では決定的である。計算量 $O(\log n)$
