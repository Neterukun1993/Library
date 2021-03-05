---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_1_C.test.py
    title: TestCase/AOJ/ALDS1_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def is_prime(x):\n    if x == 2:\n        return True\n    if x == 1 or x\
    \ % 2 == 0:\n        return False\n    for k in range(3, int(x ** 0.5) + 1, 2):\n\
    \        if x % k == 0:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/is_prime.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_1_C.test.py
documentation_of: NumberTheory/Prime/is_prime.py
layout: document
title: "\u78BA\u7387\u7684\u7D20\u6570\u5224\u5B9A (\u30D5\u30A7\u30EB\u30DE\u30FC\
  \u30C6\u30B9\u30C8)"
---

## 概要
フェルマーの小定理の対偶を用いて確率的素数判定を行うアルゴリズム。

###### フェルマーの小定理
素数 $p$ と互いに素な整数 $a$ に対して、

$$a^{p-1} \equiv 1 \pmod{p}$$

が成り立つ。
  
###### フェルマーの小定理の対偶
整数 $n$ と互いに素な整数 $a$ に対して、

$$a^{n-1} \not\equiv 1 \pmod{n}$$

であるならば $n$ は合成数。

フェルマーテストでは、$n$ と互いに素な整数 $a$ をランダムに選び、$a^{n-1} \not\equiv 1 \pmod{n}$ ならば $n$ を合成数、$a^{n-1} \equiv 1 \pmod{n}$ ならば $n$ を確率的素数と判定する。

###### 擬素数
素数ではないにもかかわらず確率的素数と判定される合成数を擬素数という。例えば $n = 341$、$a = 2$ に対して

$$2^{340} \equiv 1 \pmod{341}$$

となる。この場合、$341$ は素数ではない ($341 = 11 × 3$) にもかかわらず確率的素数と判定される。

###### カーマイケル数
複数の $a$ に対してフェルマーテストを行うことで、素数判定の正確度を向上させる。 例えば $n = 341$、$a = 5$ に対して

$$5^{340} \equiv 67 \not\equiv 1 \pmod{341}$$

となるので、この場合は $341$ を合成数と判定できる。しかしながら、すべての $a$ に対してフェルマーテストを通過する合成数が存在し、これをカーマイケル数という。カーマイケル数は小さい方から $561, 1105, 1729, \dots$ であり、無数に存在する ([OEIS A002997](https://oeis.org/A002997))。 

## 使い方
`fermat_test(n: int) -> bool`  
`n` の確率的素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。カーマイケル数は素数ではないにもかかわらず必ず `True` を返すので注意。計算量 $O(\log n)$
