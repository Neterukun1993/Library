---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/enumerate_palindromes.test.py
    title: TestCase/LibraryChecker/enumerate_palindromes.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Manacher:\n    def __init__(self, s):\n        self.s = s\n       \
    \ self.t = [\"#\"]  # \"#\" must not include in s\n        for char in s:\n  \
    \          self.t.append(char)\n            self.t.append(\"#\")\n        self.n\
    \ = len(self.t)\n        self.len_p = [0] * self.n\n        self.build()\n\n \
    \   def build(self):\n        i, j = 0, 0\n        while i < self.n:\n       \
    \     while i - j >= 0 and i + j < self.n and self.t[i - j] == self.t[i + j]:\n\
    \                j += 1\n            self.len_p[i] = j\n            k = 1\n  \
    \          while i - k >= 0 and i + k < self.n and k + self.len_p[i - k] < j:\n\
    \                self.len_p[i + k] = self.len_p[i - k]\n                k += 1\n\
    \            i += k\n            j -= k\n        self.len_p = [val - 1 for val\
    \ in self.len_p]\n\n    def longest(self):\n        max_len, center_idx = max((l,\
    \ i) for i, l in enumerate(self.len_p))\n        return self.s[(center_idx - max_len)\
    \ // 2: (center_idx + max_len) // 2]\n"
  dependsOn: []
  isVerificationFile: false
  path: String/Manacher.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/enumerate_palindromes.test.py
documentation_of: String/Manacher.py
layout: document
title: "\u6700\u9577\u56DE\u6587 (Manacher\u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\
  )"
---
