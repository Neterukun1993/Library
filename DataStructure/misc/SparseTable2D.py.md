---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable2D:\n    def __init__(self, matrix, op):\n        self.h\
    \ = len(matrix)\n        self.w = len(matrix[0])\n        self.op = op\n     \
    \   self.lg_h = self.h.bit_length()\n        self.lg_w = self.w.bit_length()\n\
    \n        self.lg_tbl = [0] * (max(self.h, self.w) + 1)\n        for i in range(2,\
    \ len(self.lg_tbl)):\n            self.lg_tbl[i] = self.lg_tbl[i // 2] + 1\n\n\
    \        self.sp_tbl = [[] * self.lg_w for _ in range(self.lg_h)]\n        self.sp_tbl[0].append(matrix)\n\
    \n        for lv_h in range(self.lg_h - 1):\n            dh = 1 << lv_h\n    \
    \        data = [[0] * self.w for _ in range(self.h)]\n            for i in range(self.h\
    \ - dh * 2 + 1):\n                for j in range(self.w):\n                  \
    \  u = self.sp_tbl[lv_h][0][i][j]\n                    d = self.sp_tbl[lv_h][0][i\
    \ + dh][j]\n                    data[i][j] = self.op(u, d)\n            self.sp_tbl[lv_h\
    \ + 1].append(data)\n\n        for lv_w in range(self.lg_w - 1):\n           \
    \ dw = 1 << lv_w\n            data = [[0] * self.w for _ in range(self.h)]\n \
    \           for i in range(self.h):\n                for j in range(self.w - dw\
    \ * 2 + 1):\n                    l = self.sp_tbl[0][lv_w][i][j]\n            \
    \        r = self.sp_tbl[0][lv_w][i][j + dw]\n                    data[i][j] =\
    \ self.op(l, r)\n            self.sp_tbl[0].append(data)\n\n        for lv_h in\
    \ range(self.lg_h - 1):\n            dh = 1 << lv_h\n            for lv_w in range(self.lg_w\
    \ - 1):\n                dw = 1 << lv_w\n                data = [[0] * self.w\
    \ for i in range(self.h)]\n                for i in range(self.h - dh * 2 + 1):\n\
    \                    for j in range(self.w - dw * 2 + 1):\n                  \
    \      ul = self.sp_tbl[lv_h][lv_w][i][j]\n                        ur = self.sp_tbl[lv_h][lv_w][i][j\
    \ + dw]\n                        dl = self.sp_tbl[lv_h][lv_w][i + dh][j]\n   \
    \                     dr = self.sp_tbl[lv_h][lv_w][i + dh][j + dw]\n         \
    \               data[i][j] = self.op(self.op(self.op(ul, ur), dl), dr)\n     \
    \           self.sp_tbl[lv_h + 1].append(data)\n\n    def fold(self, hl, hr, wl,\
    \ wr):\n        lv_h = self.lg_tbl[hr - hl]\n        lv_w = self.lg_tbl[wr - wl]\n\
    \        ul = self.sp_tbl[lv_h][lv_w][hl][wl]\n        ur = self.sp_tbl[lv_h][lv_w][hl][wr\
    \ - (1 << lv_w)]\n        dl = self.sp_tbl[lv_h][lv_w][hr - (1 << lv_h)][wl]\n\
    \        dr = self.sp_tbl[lv_h][lv_w][hr - (1 << lv_h)][wr - (1 << lv_w)]\n  \
    \      return self.op(self.op(self.op(ul, ur), dl), dr)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/SparseTable2D.py
  requiredBy: []
  timestamp: '2021-01-15 08:16:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/misc/SparseTable2D.py
layout: document
redirect_from:
- /library/DataStructure/misc/SparseTable2D.py
- /library/DataStructure/misc/SparseTable2D.py.html
title: DataStructure/misc/SparseTable2D.py
---
