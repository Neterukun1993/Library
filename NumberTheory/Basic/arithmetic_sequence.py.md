---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/arithmetic_sequence.unittest.test.py
    title: TestCase/unittest/arithmetic_sequence.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Arithmetic:\n    @staticmethod\n    def get(a0, d, i):\n        return\
    \ i * a0 + d\n\n    @staticmethod\n    def general_term(i, ai, j, aj):\n     \
    \   def gcd(a, b):\n            while b: a, b = b, a % b\n            return a\n\
    \n        assert(i != j)\n        if i > j:\n            i, j = j, i\n       \
    \ gcd_ = gcd(abs(j * ai - i * aj), j - i)\n        rational_a0 = ((j * ai - i\
    \ * aj) // gcd_, (j - i) // gcd_)\n        gcd_ = gcd(abs(aj - ai), j - i)\n \
    \       rational_d = ((aj - ai) // gcd_, (j - i) // gcd_)\n        return rational_a0,\
    \ rational_d\n\n    @staticmethod\n    def sum(a0, d, r):\n        return r *\
    \ a0 + d * (r - 1) * r // 2\n\n    @staticmethod\n    def range_sum(a0, d, l,\
    \ r):\n        return Arithmetic.sum(a0, d, r) - Arithmetic.sum(a0, d, l)\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Basic/arithmetic_sequence.py
  requiredBy: []
  timestamp: '2022-01-21 18:13:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/arithmetic_sequence.unittest.test.py
documentation_of: NumberTheory/Basic/arithmetic_sequence.py
layout: document
title: "\u7B49\u5DEE\u6570\u5217"
---

## 概要
等差数列に関する基本的な公式

## 使い方
`Arithmetic.get(a0: int, d: int, i: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について $a_i$ を返す。計算量 $O(1)$

`Arithmetic.general_term(i: int, ai: int, j: int, aj: int) -> Tuple[Tuple[int, int], Tuple[int, int]]`  
$a_i$ と $a_j$ を与えたときの、等差数列の初項 $a_0$ 公差 $d$ を返す。$a_0$ と $d$ はそれぞれ (分母, 分子) を表すタプルで返される。計算量 $O(1)$

`Arithmetic.sum(a0: int, d: int, r: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について、$a_0 + a_{1} + \ldots + a_{r-1}$ を返す。計算量 $O(1)$

`Arithmetic.range_sum(a0: int, d: int, l: int, r: int) -> int`  
初項 $a_0$ 公差 $d$ の等差数列について、$a_l + a_{l+1} + \ldots + a_{r-1}$ を返す。計算量 $O(1)$
