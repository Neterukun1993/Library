---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_14_B.test.py
    title: TestCase\AOJ\ALDS1_14_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0430.RollingHash.test.py
    title: TestCase\yukicoder\yuki0430.RollingHash.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollingHash:\r\n    def __init__(self, string):\r\n        self.n =\
    \ len(string)\r\n        self.BASE = 1234\r\n        self.MASK30 = (1 << 30) -\
    \ 1\r\n        self.MASK31 = (1 << 31) - 1\r\n        self.MASK61 = (1 << 61)\
    \ - 1\r\n        self.MOD = self.MASK61\r\n        self.hash = [0] * (self.n +\
    \ 1)\r\n        self.pow = [1] * (self.n + 1)\r\n\r\n        for i, char in enumerate(string):\r\
    \n            self.hash[i + 1] = self.calc_mod(self.mul(self.hash[i], self.BASE)\r\
    \n                                             + ord(char))\r\n            self.pow[i\
    \ + 1] = self.calc_mod(self.mul(self.pow[i], self.BASE))\r\n\r\n    def calc_mod(self,\
    \ x):\r\n        xu = x >> 61\r\n        xd = x & self.MASK61\r\n        x = xu\
    \ + xd\r\n        if x >= self.MOD:\r\n            x -= self.MOD\r\n        return\
    \ x\r\n\r\n    def mul(self, a, b):\r\n        au = a >> 31\r\n        ad = a\
    \ & self.MASK31\r\n        bu = b >> 31\r\n        bd = b & self.MASK31\r\n  \
    \      mid = ad * bu + au * bd\r\n        midu = mid >> 30\r\n        midd = mid\
    \ & self.MASK30\r\n        return self.calc_mod(au * bu * 2 + midu + (midd <<\
    \ 31) + ad * bd)\r\n\r\n    def get_hash(self, l, r):\r\n        res = self.calc_mod(self.hash[r]\r\
    \n                            - self.mul(self.hash[l], self.pow[r - l]))\r\n \
    \       return res\r\n\r\n    def merge(self, h1, h2, length2):\r\n        return\
    \ self.calc_mod(self.mul(h1, self.pow[length2]) + h2)\r\n\r\n    def get_lcp(self,\
    \ l1, r1, l2, r2):\r\n        ng = min(r1 - l1, r2 - l2) + 1\r\n        ok = 0\r\
    \n        while abs(ok - ng) > 1:\r\n            mid = (ok + ng) // 2\r\n    \
    \        if self.get_hash(l1, l1 + mid) == self.get_hash(l2, l2 + mid):\r\n  \
    \              ok = mid\r\n            else:\r\n                ng = mid\r\n \
    \       return ok\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\RollingHash.py
  requiredBy: []
  timestamp: '2021-01-23 23:52:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_14_B.test.py
  - TestCase\yukicoder\yuki0430.RollingHash.test.py
documentation_of: String\RollingHash.py
layout: document
title: "\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
---
