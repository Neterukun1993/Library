---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/1068.test.py
    title: TestCase/AOJ/1068.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable2D:\n    def __init__(self, matrix, op):\n        h = len(matrix)\n\
    \        w = len(matrix[0])\n        self.op = op\n        lg_h = h.bit_length()\n\
    \        lg_w = w.bit_length()\n\n        self.lg_tbl = [0] * (max(h, w) + 1)\n\
    \        for i in range(2, len(self.lg_tbl)):\n            self.lg_tbl[i] = self.lg_tbl[i\
    \ // 2] + 1\n\n        self.sp_tbl = [[] * lg_w for _ in range(lg_h)]\n      \
    \  self.sp_tbl[0].append(matrix)\n\n        for lv_h in range(lg_h - 1):\n   \
    \         dh = 1 << lv_h\n            data = [[0] * w for _ in range(h - dh *\
    \ 2 + 1)]\n            tbl = self.sp_tbl[lv_h][0]\n            for i in range(h\
    \ - dh * 2 + 1):\n                for j in range(w):\n                    data[i][j]\
    \ = op(tbl[i][j], tbl[i + dh][j])\n            self.sp_tbl[lv_h + 1].append(data)\n\
    \n        for lv_w in range(lg_w - 1):\n            dw = 1 << lv_w\n         \
    \   data = [[0] * (w - dw * 2 + 1) for _ in range(h)]\n            tbl = self.sp_tbl[0][lv_w]\n\
    \            for i in range(h):\n                for j in range(w - dw * 2 + 1):\n\
    \                    data[i][j] = op(tbl[i][j], tbl[i][j + dw])\n            self.sp_tbl[0].append(data)\n\
    \n        for lv_h in range(lg_h - 1):\n            dh = 1 << lv_h\n         \
    \   for lv_w in range(lg_w - 1):\n                dw = 1 << lv_w\n           \
    \     data = [[0] * (w - dw * 2 + 1) for _ in range(h - dh * 2 + 1)]\n       \
    \         tbl = self.sp_tbl[lv_h][lv_w]\n                for i in range(h - dh\
    \ * 2 + 1):\n                    for j in range(w - dw * 2 + 1):\n           \
    \             # \u4E8C\u9805\u6F14\u7B97\u3067\u306F\u306A\u3044\n           \
    \             data[i][j] = op(tbl[i][j], tbl[i][j + dw], tbl[i + dh][j], tbl[i\
    \ + dh][j + dw])\n                self.sp_tbl[lv_h + 1].append(data)\n\n    def\
    \ fold(self, hl, hr, wl, wr):\n        lv_h = self.lg_tbl[hr - hl]\n        lv_w\
    \ = self.lg_tbl[wr - wl]\n        tbl = self.sp_tbl[lv_h][lv_w]\n        ul =\
    \ tbl[hl][wl]\n        ur = tbl[hl][wr - (1 << lv_w)]\n        dl = tbl[hr - (1\
    \ << lv_h)][wl]\n        dr = tbl[hr - (1 << lv_h)][wr - (1 << lv_w)]\n      \
    \  return self.op(ul, ur, dl, dr)  # \u4E8C\u9805\u6F14\u7B97\u3067\u306F\u306A\
    \u3044\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/SparseTable2D.py
  requiredBy: []
  timestamp: '2021-02-14 12:02:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/1068.test.py
documentation_of: DataStructure/misc/SparseTable2D.py
layout: document
title: "\u4E8C\u6B21\u5143Sparse Table"
---

## 概要
構築を $O(hw\log h\log w)$、矩形畳み込みを $O(1)$ で行える二次元データ構造。畳み込みは半群 + 冪等性を要請する。定数倍が重いので注意。

## 使い方
`SparseTable(matrix: Sequence[Sequence[Any]], op: Callable[[Any, Any], Any])`  
大きさ $h × w$ の `matrix` を初期値とした 二次元 Sparse Table を構築する。`op` は畳み込み計算で用いる演算子であり、定数倍改善のため引数を 4 つ取ることがあるので注意。計算量 $O(hw\log h\log w)$

- `fold(hl: int, hr: int, wl: int, wr: int) -> Any`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の畳み込み結果を返す。計算量 $O(1)$
