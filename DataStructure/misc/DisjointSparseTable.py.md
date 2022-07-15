---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/static_range_sum.DisjointSparseTable.test.py
    title: TestCase/LibraryChecker/static_range_sum.DisjointSparseTable.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/staticrmq.DisjointSparseTable.test.py
    title: TestCase/LibraryChecker/staticrmq.DisjointSparseTable.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DisjointSparseTable:\n    def __init__(self, array, op):\n        self.n\
    \ = len(array)\n        self.op = op\n        self.row_size = self.n.bit_length()\n\
    \        self.log_tbl = [0] * (1 << self.row_size)\n        for i in range(2,\
    \ 1 << self.row_size):\n            self.log_tbl[i] = self.log_tbl[i // 2] + 1\n\
    \n        self.sp_tbl = [[0] * self.n for _ in range(self.row_size)]\n       \
    \ for i, val in enumerate(array):\n            self.sp_tbl[0][i] = val\n     \
    \   for row in range(1, self.row_size):\n            shift = 1 << row\n      \
    \      l = 0\n            while l < self.n:\n                mid = l + shift\n\
    \                t = min(mid, self.n)\n                self.sp_tbl[row][t - 1]\
    \ = array[t - 1]\n                for k in reversed(range(l, t - 1)):\n      \
    \              self.sp_tbl[row][k] = self.op(array[k], self.sp_tbl[row][k + 1])\n\
    \                if self.n <= t:\n                    break\n                r\
    \ = min(mid + shift, self.n)\n                self.sp_tbl[row][t] = array[t]\n\
    \                for k in range(t + 1, r):\n                    self.sp_tbl[row][k]\
    \ = self.op(self.sp_tbl[row][k - 1], array[k])\n                l = mid + shift\n\
    \n    def fold(self, l, r):\n        r -= 1\n        if l == r:\n            return\
    \ self.sp_tbl[0][l]\n        p = self.log_tbl[l ^ r]\n        return self.op(self.sp_tbl[p][l],\
    \ self.sp_tbl[p][r])\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/DisjointSparseTable.py
  requiredBy: []
  timestamp: '2021-01-03 11:00:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/staticrmq.DisjointSparseTable.test.py
  - TestCase/LibraryChecker/static_range_sum.DisjointSparseTable.test.py
documentation_of: DataStructure/misc/DisjointSparseTable.py
layout: document
title: Disjoint Sparse Table
---

## 概要
構築を $O(n\log n)$、区間畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群を要請する。

## 使い方
`DisjointSparseTable(array: Sequence[Any], op: Callable[[Any, Any], Any])`  
`array` を初期値とした Disjoint Sparse Table を構築する。`op` は畳み込み計算で用いる二項演算子である。計算量 $O(n\log n)$

- `fold(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

## 参考
[Disjoint Sparse Table と セグ木に関するポエム](https://noshi91.hatenablog.com/entry/2018/05/08/183946)
