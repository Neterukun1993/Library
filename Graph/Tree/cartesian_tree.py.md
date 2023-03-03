---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/cartesian_tree.test.py
    title: TestCase/LibraryChecker/cartesian_tree.test.py
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
  code: "def cartesian_tree(arr):\n    n = len(arr)\n    par = [-1] * n\n    stack\
    \ = []\n    for i in range(n):\n        prv_i = -1\n        while stack and arr[i]\
    \ < arr[stack[-1]]:\n            prv_i = stack.pop()\n        if prv_i != -1:\n\
    \            par[prv_i] = i\n        if stack:\n            par[i] = stack[-1]\n\
    \        stack.append(i)\n    return par\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/cartesian_tree.py
  requiredBy: []
  timestamp: '2021-02-03 22:14:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/cartesian_tree.test.py
documentation_of: Graph/Tree/cartesian_tree.py
layout: document
title: Cartesian Tree
---

## 概要
Cartesian Tree を求めるアルゴリズム。

## 使い方
`cartesian_tree(arr: Sequence[int]) -> List[int]`  
dinstinct な数列 `arr` から誘導される Cartesian Tree を求め、各頂点の親の配列を返す。計算量 $O(V)$

## 参考
- [列を最小値で分割して再帰するパターンと Cartesian tree - うさぎ小屋](https://kimiyuki.net/blog/2020/07/27/recursion-on-cartesian-tree/)