---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/montmort_number_mod.test.py
    title: TestCase/LibraryChecker/montmort_number_mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def montmort_number(n, MOD):\n    dp = [0] * (n + 1)\n    if n >= 2:\n  \
    \      dp[2] = 1\n    for i in range(3, n + 1):\n        dp[i] = (i - 1) * (dp[i\
    \ - 1] + dp[i - 2])\n        dp[i] %= MOD\n    return dp\n\n\ndef montmort_number2(n,\
    \ MOD):\n    dp = [0] * (n + 1)\n    for i in range(1, n):\n        dp[i + 1]\
    \ = (i + 1) * dp[i] + (-1) ** ((i + 1) & 1)\n        dp[i + 1] %= MOD\n    return\
    \ dp\n"
  dependsOn: []
  isVerificationFile: false
  path: Combination/montmort_number.py
  requiredBy: []
  timestamp: '2021-01-27 22:05:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/montmort_number_mod.test.py
documentation_of: Combination/montmort_number.py
layout: document
title: "\u30E2\u30F3\u30E2\u30FC\u30EB\u6570 (\u5B8C\u5168\u9806\u5217)"
---
## 概要
整数 $1, 2, \dots , n$ を並び替えてできる順列において、$i$ 番目 ($1 \le i \le n$) が $i$ でない順列を完全順列 (撹拌順列) という。完全順列となる通り数 $a_n$ をモンモール数という。

モンモール数は以下の漸化式で考えることができる。

$$a_n=(n-1)(a_{n-1}+a_{n-2})$$

また、一般項を計算すると以下の式となる。

$$a_n=n!\sum_{k=2}^n\frac{(-1)^k}{k!}$$

漸化式の導出と包除原理による一般項の導出は [高校数学の美しい物語](https://manabitimes.jp/math/612) が分かりやすい。具体的な数列は OEIS [A000166](https://oeis.org/A000166) を参照。

## 使い方
`montmort_number(n: int, MOD: int) -> List[int]`  
`MOD` 上での第 `n` 項までのモンモール数のリストを返す。計算量 $O(n)$

`montmort_number2(n: int, MOD: int) -> List[int]`  
`MOD` 上での第 `n` 項までのモンモール数のリストを返す。計算量 $O(n)$

## 備考
漸化式の計算のイメージ

<img src="https://Neterukun1993.github.io/Library/montmort_number.png" width="600">
