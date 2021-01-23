---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\suffixarray.nlogn.test.py
    title: TestCase\LibraryChecker\suffixarray.nlogn.test.py
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
    \ len(string)\r\n        self.sa = [0] * (self.n + 1)\r\n        self.lcp = [0]\
    \ * (self.n + 1)\r\n        if type(string[0]) == str:\r\n            array =\
    \ [ord(char) for char in string]\r\n        else:\r\n            array = string\r\
    \n        array = self.compress(array)\r\n        self.build_SA(array)\r\n   \
    \     self.build_LCP(array)\r\n\r\n    def compress(self, array):\r\n        memo\
    \ = {val: idx for idx, val in enumerate(sorted(set(array)))}\r\n        array\
    \ = [memo[val] + 1 for val in array]\r\n        return array\r\n\r\n    def build_SA(self,\
    \ array):\r\n        array = array + [0]\r\n        n = len(array)\r\n       \
    \ c = [0] * n\r\n        cnt = [0] * n\r\n        cn = [0] * n\r\n\r\n       \
    \ for val in array:\r\n            cnt[val] += 1\r\n        for i in range(1,\
    \ n):\r\n            cnt[i] += cnt[i - 1]\r\n        for i, val in enumerate(array):\r\
    \n            cnt[val] -= 1\r\n            self.sa[cnt[val]] = i\r\n\r\n     \
    \   c[self.sa[0]] = 0\r\n        classes = 1\r\n        for i in range(1, n):\r\
    \n            if array[self.sa[i]] != array[self.sa[i - 1]]:\r\n             \
    \   classes += 1\r\n            c[self.sa[i]] = classes - 1\r\n\r\n        k =\
    \ 0\r\n        while (1 << k) < n:\r\n            shift = 1 << k\r\n         \
    \   pn = [(self.sa[i] - shift) % n for i in range(n)]\r\n\r\n            for i\
    \ in range(classes):\r\n                cnt[i] = 0\r\n            for i in pn:\r\
    \n                cnt[c[i]] += 1\r\n            for i in range(1, classes):\r\n\
    \                cnt[i] += cnt[i - 1]\r\n            for i in reversed(pn):\r\n\
    \                cnt[c[i]] -= 1\r\n                self.sa[cnt[c[i]]] = i\r\n\r\
    \n            prv_idx = self.sa[0]\r\n            cn[prv_idx] = 0\r\n        \
    \    classes = 1\r\n            for cur_idx in self.sa[1:]:\r\n              \
    \  cur = c[cur_idx], c[(cur_idx + shift) % n]\r\n                prv = c[prv_idx],\
    \ c[(prv_idx + shift) % n]\r\n                if cur != prv:\r\n             \
    \       classes += 1\r\n                cn[cur_idx] = classes - 1\r\n        \
    \        prv_idx = cur_idx\r\n            c, cn = cn, c\r\n            k += 1\r\
    \n\r\n    def build_LCP(self, array):\r\n        rank = [0] * (self.n + 1)\r\n\
    \        for i, val in enumerate(self.sa):\r\n            rank[val] = i\r\n  \
    \      h = 0\r\n        for i, rk in enumerate(rank):\r\n            j = self.sa[rk\
    \ - 1]\r\n            if h > 0:\r\n                h -= 1\r\n            while\
    \ j + h < self.n and i + h < self.n:\r\n                if array[j + h] != array[i\
    \ + h]:\r\n                    break\r\n                else:\r\n            \
    \        h += 1\r\n            self.lcp[rk - 1] = h\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\SA_nlogn.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\suffixarray.nlogn.test.py
documentation_of: String\SA_nlogn.py
layout: document
title: "\u63A5\u5C3E\u8F9E\u914D\u5217 ($\\mathrm{O}(N (\\log N))$)"
---
