---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Heap\RandomizedMeldableHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Randomized Meldable Heap)"
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
  code: "def xorshift32():\r\n    y = 2463534242\r\n    def inner():\r\n        nonlocal\
    \ y\r\n        y = y ^ (y << 13 & 0xFFFFFFFF)\r\n        y = y ^ (y >> 17 & 0xFFFFFFFF)\r\
    \n        y = y ^ (y << 5 & 0xFFFFFFFF)\r\n        return y & 0xFFFFFFFF\r\n \
    \   return inner\r\n"
  dependsOn: []
  isVerificationFile: false
  path: misc\xorshift.py
  requiredBy:
  - DataStructure\Heap\RandomizedMeldableHeap.py
  timestamp: '2021-01-19 22:36:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: misc\xorshift.py
layout: document
title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
---
