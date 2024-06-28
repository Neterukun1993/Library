---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/catalan.unittest.test.py
    title: TestCase/unittest/catalan.unittest.test.py
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
  code: "from Combination.modinv_combination import Combination\n\n\nMOD = 10 ** 9\
    \ + 7\ncomb = Combination(10 ** 6 + 10, MOD)\n\n\ndef catalan(n):\n    return\
    \ comb.comb(2 * n, n) * comb.inv(n + 1) % comb.MOD\n\n\ndef catalan_trapezoid(n,\
    \ k, m=1):\n    if 0 <= k < m:\n        return comb.comb(n + k, k)\n    elif m\
    \ <= k < n + m:\n        return (comb.comb(n + k, k) - comb.comb(n + k, k - m))\
    \ % comb.MOD\n    else:\n        return 0\n"
  dependsOn:
  - Combination/modinv_combination.py
  isVerificationFile: false
  path: Combination/catalan.py
  requiredBy: []
  timestamp: '2021-09-08 22:15:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/catalan.unittest.test.py
documentation_of: Combination/catalan.py
layout: document
title: "\u30AB\u30BF\u30E9\u30F3\u6570"
---
## 概要

### カタラン数 (Catalan number)
カタラン数とは、様々な数え上げに現れる数列である。$n$ 番目のカタラン数の一般項は、以下の通りとなる。

$$C_n=\frac{1}{n+1}\binom{2n}{n}$$

数え上げにおいて、次のような意味付けがなされる。
- 対角線を跨がないグリッド上の最短経路
- 括弧列
- 多角形の三角形分割

### カタランの三角形 (Catalan's triangle)
カタランの三角形とは、カタラン数の一般化である。$C(n, k)$ は、$n$ 個の X と $k$ 個 Y を一列に並べたとき、全ての接頭辞について Y の個数が X の個数を超えないような、並べ方の場合の数である。一般項は、以下の通りとなる。

$$C(n, k)=\frac{n-k+1}{n+1}\binom{n+k}{n}$$

$n = k$ のとき、$C(n, n) = C_n$ となる。

### カタランの台形 (Catalan's trapezoid)
カタランの台形は、カタランの三角形の一般化である。$C_m(n, k)$ は、
$n$ 個の X と $k$ 個の Y の数を一列に並べたとき、全ての接頭辞について Y の個数が X の個数を $m - 1$ 以上超えないような、並べ方の場合の数である。一般項は、以下の通りとなる。

$m = 1$ のとき、$C_1(n, k) = C(n, k)$ となる。

## 備考
カタラン数 (グリッド上の最短経路数)

<img src="https://Neterukun1993.github.io/Library/catalan_number.png" width="400">

カタランの台形 (グリッド上の最短経路数)

<img src="https://Neterukun1993.github.io/Library/catalan_trapezoid.png" width="400">

## 使い方
`catalan(n: int) -> int`  
$n$ 番目のカタラン数を返す。計算量 $O(1)$

`catalan_trapezoid(n: int, k: int, m: int = 1) -> int`  
$C_m(n, k)$ を返す。計算量 $O(1)$
