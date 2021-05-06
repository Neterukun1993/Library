---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_1_B.test.py
    title: TestCase/AOJ/ALDS1_1_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/NTL_1_C.test.py
    title: TestCase/AOJ/NTL_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a\n\n\n\
    def lcm(a, b):\n    return (a * b) // gcd(a, b)\n\n\ndef all_gcd(array):\n   \
    \ n = len(array)\n    ans = array[0]\n    for i in range(1, n):\n        ans =\
    \ gcd(ans, array[i])\n    return ans\n\n\ndef all_lcm_int(array):\n    ans = array[0]\n\
    \    for i in range(1, len(array)):\n        ans = (ans * array[i]) // gcd(ans,\
    \ array[i])\n    return ans\n\n\ndef all_lcm_dict(array):\n    primes = {}\n \
    \   for num in array:\n        for k in range(2, int(num ** 0.5) + 1):\n     \
    \       cnt = 0\n            while num % k == 0:\n                cnt += 1\n \
    \               num //= k\n            if cnt != 0:\n                if k not\
    \ in primes:\n                    primes[k] = cnt\n                else:\n   \
    \                 primes[k] = max(cnt, primes[k])\n        if num != 1:\n    \
    \        if num not in primes:\n                primes[num] = 1\n    return primes\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Basic/gcd_lcm.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_1_B.test.py
  - TestCase/AOJ/NTL_1_C.test.py
documentation_of: NumberTheory/Basic/gcd_lcm.py
layout: document
title: "\u6700\u5927\u516C\u7D04\u6570\u3068\u6700\u5C0F\u516C\u500D\u6570"
---

## 概要
最大公約数 (greatest common divisor, GCD) と最小公倍数 (east common multiple, lcm) を求めるアルゴリズム。

## 使い方
`gcd(a: int, b: int) -> int`  
`a` と `b` の最大公約数を返す。計算量 $O(\log \min(a, b))$

`lcm(a: int, b: int) -> int`  
`a` と `b` の最小公倍数を返す。計算量 $O(\log \min(a, b))$

`all_gcd(array: Iterable[int]) -> int`  
`array` の全要素の最小公約数を返す。`n = len(array)`、`a = min(array)` とすると、計算量 $O(n + \log a)$

`all_lcm_int(array: Iterable[int]) -> int`  
`array` の全要素の最大公倍数を返す。`n = len(array)`、`a = array[0] * array[1] * ... * array[n - 1]` とすると、計算量 $O(n + \log a)$

`all_lcm_dict(array: Iterable[int]) -> Dict[int, int]`  
`array` 全要素の最大公倍数を (key, value) = (素因数, 素因数の個数) とした辞書で返す。`n = len(array)`、`a = max(array)` とすると、計算量 $O(n\sqrt a)$
