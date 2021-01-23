---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\zalgorithm.test.py
    title: TestCase\LibraryChecker\zalgorithm.test.py
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
  code: "def z_algorithm(s):\r\n    res = [0] * len(s)\r\n    res[0] = len(s)\r\n\
    \    i, j = 1, 0\r\n    while i < len(s):\r\n        while i + j < len(s) and\
    \ s[j] == s[i + j]:\r\n            j += 1\r\n        res[i] = j\r\n        if\
    \ j == 0:\r\n            i += 1\r\n            continue\r\n        k = 1\r\n \
    \       while i + k < len(s) and k + res[k] < j:\r\n            res[i + k] = res[k]\r\
    \n            k += 1\r\n        i, j = i + k, j - k\r\n    return res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: String\z_algorithm.py
  requiredBy: []
  timestamp: '2021-01-05 22:30:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\zalgorithm.test.py
documentation_of: String\z_algorithm.py
layout: document
title: Z algorithm
---
