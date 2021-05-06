---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_1_D.test.py
    title: TestCase/AOJ/DPL_1_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, bisect_right\n\n\ndef lis(array, strict=True):\n\
    \    lis_array = [array[0]]\n    for val in array[1:]:\n        if val > lis_array[-1]\
    \ or (not strict and val == lis_array):\n            lis_array.append(val)\n \
    \       else:\n            lis_array[bisect_left(lis_array, val)] = val\n\n  \
    \  return lis_array\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/lis.py
  requiredBy: []
  timestamp: '2021-05-06 13:26:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_1_D.test.py
documentation_of: DP/lis.py
layout: document
title: "\u6700\u9577\u5897\u52A0\u90E8\u5206\u5217 (longest increasing subsequence)"
---

## 概要
最長増加部分列を求めるアルゴリズム。

## 使い方
`lis(array: Sequence[int], strict: bool = True) -> List[int]`  
`array` に対する最長増加部分列を返す。`strict=False` とすると、広義最長増加部分列を返す。計算量 $O(N \log N)$
