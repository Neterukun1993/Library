---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable2D:\r\n    def __init__(self, matrix, op):\r\n        self.h\
    \ = len(matrix)\r\n        self.w = len(matrix[0])\r\n        self.op = op\r\n\
    \        self.lg_h = self.h.bit_length()\r\n        self.lg_w = self.w.bit_length()\r\
    \n\r\n        self.lg_tbl = [0] * (max(self.h, self.w) + 1)\r\n        for i in\
    \ range(2, len(self.lg_tbl)):\r\n            self.lg_tbl[i] = self.lg_tbl[i //\
    \ 2] + 1\r\n\r\n        self.sp_tbl = [[] * self.lg_w for _ in range(self.lg_h)]\r\
    \n        self.sp_tbl[0].append(matrix)\r\n\r\n        for lv_h in range(self.lg_h\
    \ - 1):\r\n            dh = 1 << lv_h\r\n            data = [[0] * self.w for\
    \ _ in range(self.h)]\r\n            for i in range(self.h - dh * 2 + 1):\r\n\
    \                for j in range(self.w):\r\n                    u = self.sp_tbl[lv_h][0][i][j]\r\
    \n                    d = self.sp_tbl[lv_h][0][i + dh][j]\r\n                \
    \    data[i][j] = self.op(u, d)\r\n            self.sp_tbl[lv_h + 1].append(data)\r\
    \n\r\n        for lv_w in range(self.lg_w - 1):\r\n            dw = 1 << lv_w\r\
    \n            data = [[0] * self.w for _ in range(self.h)]\r\n            for\
    \ i in range(self.h):\r\n                for j in range(self.w - dw * 2 + 1):\r\
    \n                    l = self.sp_tbl[0][lv_w][i][j]\r\n                    r\
    \ = self.sp_tbl[0][lv_w][i][j + dw]\r\n                    data[i][j] = self.op(l,\
    \ r)\r\n            self.sp_tbl[0].append(data)\r\n\r\n        for lv_h in range(self.lg_h\
    \ - 1):\r\n            dh = 1 << lv_h\r\n            for lv_w in range(self.lg_w\
    \ - 1):\r\n                dw = 1 << lv_w\r\n                data = [[0] * self.w\
    \ for i in range(self.h)]\r\n                for i in range(self.h - dh * 2 +\
    \ 1):\r\n                    for j in range(self.w - dw * 2 + 1):\r\n        \
    \                ul = self.sp_tbl[lv_h][lv_w][i][j]\r\n                      \
    \  ur = self.sp_tbl[lv_h][lv_w][i][j + dw]\r\n                        dl = self.sp_tbl[lv_h][lv_w][i\
    \ + dh][j]\r\n                        dr = self.sp_tbl[lv_h][lv_w][i + dh][j +\
    \ dw]\r\n                        data[i][j] = self.op(self.op(self.op(ul, ur),\
    \ dl), dr)\r\n                self.sp_tbl[lv_h + 1].append(data)\r\n\r\n    def\
    \ fold(self, hl, hr, wl, wr):\r\n        lv_h = self.lg_tbl[hr - hl]\r\n     \
    \   lv_w = self.lg_tbl[wr - wl]\r\n        ul = self.sp_tbl[lv_h][lv_w][hl][wl]\r\
    \n        ur = self.sp_tbl[lv_h][lv_w][hl][wr - (1 << lv_w)]\r\n        dl = self.sp_tbl[lv_h][lv_w][hr\
    \ - (1 << lv_h)][wl]\r\n        dr = self.sp_tbl[lv_h][lv_w][hr - (1 << lv_h)][wr\
    \ - (1 << lv_w)]\r\n        return self.op(self.op(self.op(ul, ur), dl), dr)\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\misc\SparseTable2D.py
  requiredBy: []
  timestamp: '2021-01-15 08:16:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\misc\SparseTable2D.py
layout: document
title: "\u4E8C\u6B21\u5143Sparse Table"
---
