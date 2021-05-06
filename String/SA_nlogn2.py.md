---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/suffixarray.nlogn2.test.py
    title: TestCase/LibraryChecker/suffixarray.nlogn2.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SuffixArray:\n    def __init__(self, string):\n        self.n = len(string)\n\
    \        self.sa = [i for i in range(self.n + 1)]\n        self.lcp = [0] * (self.n\
    \ + 1)\n        if type(string[0]) == str:\n            array = [ord(char) for\
    \ char in string]\n        else:\n            array = string\n        self.build_SA(array)\n\
    \        self.build_LCP(array)\n\n    def build_SA(self, array):\n        rank\
    \ = [-1] * (2 * self.n + 1)\n        rank[0:self.n] = array\n\n        tmp = [0]\
    \ * (self.n + 1)\n        cmp_sa = lambda i: (rank[i] << 32) | (rank[i + k] +\
    \ 1)\n\n        k = 1\n        while k <= self.n:\n            self.sa.sort(key=cmp_sa)\n\
    \            val = self.sa[0]\n            tmp[val] = 0\n            for nxt_val\
    \ in self.sa[1:]:\n                tmp[nxt_val] = tmp[val] + (cmp_sa(val) < cmp_sa(nxt_val))\n\
    \                val = nxt_val\n            rank[0:self.n + 1] = tmp\n       \
    \     k <<= 1\n\n    def build_LCP(self, array):\n        rank = [0] * (self.n\
    \ + 1)\n        for i, val in enumerate(self.sa):\n            rank[val] = i\n\
    \        h = 0\n        for i, rk in enumerate(rank):\n            j = self.sa[rk\
    \ - 1]\n            if h > 0:\n                h -= 1\n            while j + h\
    \ < self.n and i + h < self.n:\n                if array[j + h] != array[i + h]:\n\
    \                    break\n                else:\n                    h += 1\n\
    \            self.lcp[rk - 1] = h\n"
  dependsOn: []
  isVerificationFile: false
  path: String/SA_nlogn2.py
  requiredBy: []
  timestamp: '2021-01-16 10:09:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/suffixarray.nlogn2.test.py
documentation_of: String/SA_nlogn2.py
layout: document
title: "\u63A5\u5C3E\u8F9E\u914D\u5217 ($\\mathrm{O}(N (\\log^2 N))$)"
---
