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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollingHash2D:\n    def __init__(self, matrix):\n        self.h = len(matrix)\n\
    \        self.w = len(matrix[0])\n        self.BASEh = 1234\n        self.BASEw\
    \ = 5678\n        self.MASK30 = (1 << 30) - 1\n        self.MASK31 = (1 << 31)\
    \ - 1\n        self.MASK61 = self.MOD = (1 << 61) - 1\n        self.hash = [[0]\
    \ * (self.w + 1) for _ in range(self.h + 1)]\n        self.ph = [1] * (self.h\
    \ + 1)\n        self.pw = [1] * (self.w + 1)\n        for i in range(self.h):\n\
    \            self.ph[i + 1] = self.calc_mod(self.mul(self.ph[i], self.BASEh))\n\
    \        for i in range(self.w):\n            self.pw[i + 1] = self.calc_mod(self.mul(self.pw[i],\
    \ self.BASEw))\n\n        for i in range(self.h):\n            for j in range(self.w):\n\
    \                res = self.mul(self.hash[i + 1][j], self.BASEw)\n           \
    \     res += self.mul(self.hash[i][j + 1], self.BASEh)\n                res -=\
    \ self.mul(self.hash[i][j], self.BASEw * self.BASEh)\n                self.hash[i\
    \ + 1][j + 1] = self.calc_mod(res + ord(matrix[i][j]))\n\n    def calc_mod(self,\
    \ x):\n        xu = x >> 61\n        xd = x & self.MASK61\n        x = xu + xd\n\
    \        if x >= self.MOD:\n            x -= self.MOD\n        return x\n\n  \
    \  def mul(self, a, b):\n        au = a >> 31\n        ad = a & self.MASK31\n\
    \        bu = b >> 31\n        bd = b & self.MASK31\n        mid = ad * bu + au\
    \ * bd\n        midu = mid >> 30\n        midd = mid & self.MASK30\n        return\
    \ self.calc_mod(au * bu * 2 + midu + (midd << 31) + ad * bd)\n\n    def get_hash(self,\
    \ hl, hr, wl, wr):\n        p, q = self.pw[wr - wl], self.ph[hr - hl]\n      \
    \  res = self.hash[hr][wr]\n        res -= self.mul(self.hash[hr][wl], p)\n  \
    \      res -= self.mul(self.hash[hl][wr], q)\n        res += self.mul(self.hash[hl][wl],\
    \ self.mul(p, q))\n        return self.calc_mod(res)\n"
  dependsOn: []
  isVerificationFile: false
  path: String/RollingHash2D.py
  requiredBy: []
  timestamp: '2021-01-24 04:01:39+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: String/RollingHash2D.py
layout: document
title: "\u4E8C\u6B21\u5143\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
---
