---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\enumerate_palindromes.test.py
    title: TestCase\LibraryChecker\enumerate_palindromes.test.py
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
  code: "class Manacher:\r\n    def __init__(self, s):\r\n        self.s = s\r\n \
    \       self.t = [\"#\"]  # \"#\" must not include in s\r\n        for char in\
    \ s:\r\n            self.t.append(char)\r\n            self.t.append(\"#\")\r\n\
    \        self.n = len(self.t)\r\n        self.len_p = [0] * self.n\r\n       \
    \ self.build()\r\n\r\n    def build(self):\r\n        i, j = 0, 0\r\n        while\
    \ i < self.n:\r\n            while i - j >= 0 and i + j < self.n and self.t[i\
    \ - j] == self.t[i + j]:\r\n                j += 1\r\n            self.len_p[i]\
    \ = j\r\n            k = 1\r\n            while i - k >= 0 and i + k < self.n\
    \ and k + self.len_p[i - k] < j:\r\n                self.len_p[i + k] = self.len_p[i\
    \ - k]\r\n                k += 1\r\n            i += k\r\n            j -= k\r\
    \n        self.len_p = [val - 1 for val in self.len_p]\r\n\r\n    def longest(self):\r\
    \n        max_len, center_idx = max((l, i) for i, l in enumerate(self.len_p))\r\
    \n        return self.s[(center_idx - max_len) // 2: (center_idx + max_len) //\
    \ 2]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\Manacher.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\enumerate_palindromes.test.py
documentation_of: String\Manacher.py
layout: document
redirect_from:
- /library\String\Manacher.py
- /library\String\Manacher.py.html
title: String\Manacher.py
---
