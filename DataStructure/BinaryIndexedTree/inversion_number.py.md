---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_5_D.test.py
    title: TestCase/AOJ/ALDS1_5_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree\n\
    \n\ndef inversion_number(array):\n    comp = {val: i for i, val in enumerate(sorted(set(array)))}\n\
    \    for i, val in enumerate(array):\n        array[i] = comp[val]\n    max_val\
    \ = max(array)\n    bit = BinaryIndexedTree(max_val + 1)\n    inv_num = 0\n  \
    \  for i in array:\n        bit.add(i, 1)\n        inv_num += bit.sum(i + 1, max_val\
    \ + 1)\n    return inv_num\n"
  dependsOn:
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/inversion_number.py
  requiredBy: []
  timestamp: '2021-01-02 16:13:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_5_D.test.py
documentation_of: DataStructure/BinaryIndexedTree/inversion_number.py
layout: document
title: "\u8EE2\u5012\u6570"
---

## 使い方
`inversion_number(array: Sequence[int]) -> int`  
`array` の転倒数を返す。計算量 $O(n\log n)$
