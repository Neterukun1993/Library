---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_1_D.test.py
    title: TestCase/AOJ/DPL_1_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/longest_increasing_subsequence.test.py
    title: TestCase/LibraryChecker/longest_increasing_subsequence.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left, bisect_right\n\n\ndef lis(array, strict=True):\n\
    \    bisect_ = bisect_left if strict else bisect_right\n    tmp = []\n    idxs\
    \ = [0] * len(array)\n\n    for i, val in enumerate(array):\n        idx = bisect_(tmp,\
    \ val)\n        if idx == len(tmp):\n            tmp.append(val)\n        else:\n\
    \            tmp[idx] = val\n        idxs[i] = idx\n\n    lis_array = []\n   \
    \ j = len(tmp) - 1\n    for i, val in reversed(list(enumerate(array))):\n    \
    \    if idxs[i] == j:\n            lis_array.append(val)\n            j -= 1\n\
    \    return lis_array[::-1]\n\n\ndef lis_index(array, strict=True):\n    lis_array\
    \ = lis(array, strict)\n    idxs = []\n\n    i = 0\n    for idx, val in enumerate(array):\n\
    \        if i < len(lis_array) and lis_array[i] == val:\n            idxs.append(idx)\n\
    \            i += 1\n    return idxs\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/lis.py
  requiredBy: []
  timestamp: '2023-03-03 23:23:30+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/longest_increasing_subsequence.test.py
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
