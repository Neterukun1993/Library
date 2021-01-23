---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\suffixarray.nlogn2.test.py
    title: TestCase\LibraryChecker\suffixarray.nlogn2.test.py
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
  code: "class SuffixArray:\r\n    def __init__(self, string):\r\n        self.n =\
    \ len(string)\r\n        self.sa = [i for i in range(self.n + 1)]\r\n        self.lcp\
    \ = [0] * (self.n + 1)\r\n        if type(string[0]) == str:\r\n            array\
    \ = [ord(char) for char in string]\r\n        else:\r\n            array = string\r\
    \n        self.build_SA(array)\r\n        self.build_LCP(array)\r\n\r\n    def\
    \ build_SA(self, array):\r\n        rank = [-1] * (2 * self.n + 1)\r\n       \
    \ rank[0:self.n] = array\r\n\r\n        tmp = [0] * (self.n + 1)\r\n        cmp_sa\
    \ = lambda i: (rank[i] << 32) | (rank[i + k] + 1)\r\n\r\n        k = 1\r\n   \
    \     while k <= self.n:\r\n            self.sa.sort(key=cmp_sa)\r\n         \
    \   val = self.sa[0]\r\n            tmp[val] = 0\r\n            for nxt_val in\
    \ self.sa[1:]:\r\n                tmp[nxt_val] = tmp[val] + (cmp_sa(val) < cmp_sa(nxt_val))\r\
    \n                val = nxt_val\r\n            rank[0:self.n + 1] = tmp\r\n  \
    \          k <<= 1\r\n\r\n    def build_LCP(self, array):\r\n        rank = [0]\
    \ * (self.n + 1)\r\n        for i, val in enumerate(self.sa):\r\n            rank[val]\
    \ = i\r\n        h = 0\r\n        for i, rk in enumerate(rank):\r\n          \
    \  j = self.sa[rk - 1]\r\n            if h > 0:\r\n                h -= 1\r\n\
    \            while j + h < self.n and i + h < self.n:\r\n                if array[j\
    \ + h] != array[i + h]:\r\n                    break\r\n                else:\r\
    \n                    h += 1\r\n            self.lcp[rk - 1] = h\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\SA_nlogn2.py
  requiredBy: []
  timestamp: '2021-01-16 10:09:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\suffixarray.nlogn2.test.py
documentation_of: String\SA_nlogn2.py
layout: document
title: "\u63A5\u5C3E\u8F9E\u914D\u5217 ($\\mathrm{O}(N (\\log^2 N))$)"
---
