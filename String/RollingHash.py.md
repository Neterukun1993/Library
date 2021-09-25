---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_14_B.test.py
    title: TestCase/AOJ/ALDS1_14_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0430.RollingHash.test.py
    title: TestCase/yukicoder/yuki0430.RollingHash.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollingHash:\n    def __init__(self, string):\n        self.n = len(string)\n\
    \        self.BASE = 1234\n        self.MASK30 = (1 << 30) - 1\n        self.MASK31\
    \ = (1 << 31) - 1\n        self.MASK61 = (1 << 61) - 1\n        self.MOD = self.MASK61\n\
    \        self.hash = [0] * (self.n + 1)\n        self.pow = [1] * (self.n + 1)\n\
    \n        for i, char in enumerate(string):\n            self.hash[i + 1] = self.calc_mod(self.mul(self.hash[i],\
    \ self.BASE)\n                                             + ord(char))\n    \
    \        self.pow[i + 1] = self.calc_mod(self.mul(self.pow[i], self.BASE))\n\n\
    \    def calc_mod(self, x):\n        xu = x >> 61\n        xd = x & self.MASK61\n\
    \        x = xu + xd\n        if x >= self.MOD:\n            x -= self.MOD\n \
    \       return x\n\n    def mul(self, a, b):\n        au = a >> 31\n        ad\
    \ = a & self.MASK31\n        bu = b >> 31\n        bd = b & self.MASK31\n    \
    \    mid = ad * bu + au * bd\n        midu = mid >> 30\n        midd = mid & self.MASK30\n\
    \        return self.calc_mod(au * bu * 2 + midu + (midd << 31) + ad * bd)\n\n\
    \    def get_hash(self, l, r):\n        res = self.calc_mod(self.hash[r]\n   \
    \                         - self.mul(self.hash[l], self.pow[r - l]))\n       \
    \ return res\n\n    def merge(self, h1, h2, length2):\n        return self.calc_mod(self.mul(h1,\
    \ self.pow[length2]) + h2)\n\n    def get_lcp(self, l1, r1, l2, r2):\n       \
    \ ng = min(r1 - l1, r2 - l2) + 1\n        ok = 0\n        while abs(ok - ng) >\
    \ 1:\n            mid = (ok + ng) // 2\n            if self.get_hash(l1, l1 +\
    \ mid) == self.get_hash(l2, l2 + mid):\n                ok = mid\n           \
    \ else:\n                ng = mid\n        return ok\n"
  dependsOn: []
  isVerificationFile: false
  path: String/RollingHash.py
  requiredBy: []
  timestamp: '2021-01-23 23:52:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0430.RollingHash.test.py
  - TestCase/AOJ/ALDS1_14_B.test.py
documentation_of: String/RollingHash.py
layout: document
title: "\u30ED\u30FC\u30EA\u30F3\u30B0\u30CF\u30C3\u30B7\u30E5"
---
