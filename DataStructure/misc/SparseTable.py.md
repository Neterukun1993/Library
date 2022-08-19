---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/staticrmq.test.py
    title: TestCase/LibraryChecker/staticrmq.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable:\n    def __init__(self, array, op):\n        self.n =\
    \ len(array)\n        self.row_size = self.n.bit_length()\n        self.op = op\n\
    \n        self.log_tbl = [0] * (self.n + 1)\n        for i in range(2, self.n\
    \ + 1):\n            self.log_tbl[i] = self.log_tbl[i // 2] + 1\n\n        self.sp_tbl\
    \ = [0] * (self.n * self.row_size)\n        for i in range(self.n):\n        \
    \    self.sp_tbl[i] = array[i]\n        for row in range(1, self.row_size):\n\
    \            prv_row = row - 1\n            for i in range(self.n - (1 << row)\
    \ + 1):\n                self.sp_tbl[row * self.n + i] = \\\n                self.op(self.sp_tbl[prv_row\
    \ * self.n + i],\n                        self.sp_tbl[prv_row * self.n + i + (1\
    \ << prv_row)])\n\n    def fold(self, l, r):\n        row = self.log_tbl[r - l]\n\
    \        return self.op(self.sp_tbl[row * self.n + l],\n                     \
    \  self.sp_tbl[row * self.n + r - (1 << row)])\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/SparseTable.py
  requiredBy: []
  timestamp: '2021-01-03 09:10:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/staticrmq.test.py
documentation_of: DataStructure/misc/SparseTable.py
layout: document
title: Sparse Table
---

## 概要
構築を $O(n\log n)$、区間畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群 + 冪等性を要請する。

## 使い方
`SparseTable(array: Sequence[Any], op: Callable[[Any, Any], Any])`  
`array` を初期値とした Sparse Table を構築する。`op` は畳み込み計算で用いる二項演算子である。計算量 $O(n\log n)$

- `fold(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$
