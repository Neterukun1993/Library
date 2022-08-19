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
  code: "import random\n\n\ndef fermat_test(n, rep=100):\n    def gcd(a, b):\n   \
    \     while b:\n            a, b = b, a % b\n        return a\n\n    if n == 1:\n\
    \        return False\n    if n == 2:\n        return True\n    for _ in range(rep):\n\
    \        a = random.randint(2, n - 1)\n        if gcd(a, n) != 1:\n          \
    \  # a \u3068 n \u304C\u4E92\u3044\u306B\u7D20\u3067\u306F\u306A\u3044\u6642\u70B9\
    \u3067 n \u306F\u5408\u6210\u6570\n            # \u30AB\u30FC\u30DE\u30A4\u30B1\
    \u30EB\u6570\u3092\u7D20\u6570\u3068\u8AA4\u5224\u5B9A\u3055\u305B\u308B\u305F\
    \u3081\u306B continue \u3057\u3066\u3044\u308B\n            continue\n       \
    \ if pow(a, n - 1, n) != 1:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/fermat_test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/Prime/fermat_test.py
layout: document
title: "\u78BA\u7387\u7684\u7D20\u6570\u5224\u5B9A (\u30D5\u30A7\u30EB\u30DE\u30FC\
  \u30C6\u30B9\u30C8)"
---

## 概要
フェルマーの小定理の対偶を用いて確率的素数判定を行うアルゴリズム。

#### フェルマーの小定理
素数 $p$ と互いに素な整数 $a$ に対して、

$$a^{p-1} \equiv 1 \pmod{p}$$

が成り立つ。
  
#### フェルマーの小定理の対偶
整数 $n$ と互いに素な整数 $a$ に対して、

$$a^{n-1} \not\equiv 1 \pmod{n}$$

であるならば $n$ は合成数。

フェルマーテストでは、$n$ と互いに素な整数 $a$ をランダムに選び、$a^{n-1} \not\equiv 1 \pmod{n}$ ならば $n$ を合成数、$a^{n-1} \equiv 1 \pmod{n}$ ならば $n$ を確率的素数と判定する。

#### 擬素数
素数ではないにもかかわらず確率的素数と判定される合成数を擬素数という。例えば $n = 341$、$a = 2$ に対して

$$2^{340} \equiv 1 \pmod{341}$$

となる。この場合、$341$ は素数ではない ($341 = 11 × 3$) にもかかわらず確率的素数と判定される。

#### カーマイケル数
複数の $a$ に対してフェルマーテストを行うことで、素数判定の正確度を向上させる。 例えば $n = 341$、$a = 5$ に対して

$$5^{340} \equiv 67 \not\equiv 1 \pmod{341}$$

となるので、この場合は $341$ を合成数と判定できる。しかしながら、すべての $a$ に対してフェルマーテストを通過する合成数が存在し、これをカーマイケル数という。カーマイケル数は小さい方から $561, 1105, 1729, \dots$ であり、無数に存在する ([OEIS A002997](https://oeis.org/A002997))。 

## 使い方
`fermat_test(n: int) -> bool`  
`n` の確率的素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。カーマイケル数は素数ではないにもかかわらず必ず `True` を返すので注意。計算量 $O(\log n)$
