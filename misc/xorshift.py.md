---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/RandomizedMeldableHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Randomized Meldable Heap)"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def xorshift32():\n    y = 2463534242\n    def inner():\n        nonlocal\
    \ y\n        y = y ^ (y << 13 & 0xFFFFFFFF)\n        y = y ^ (y >> 17 & 0xFFFFFFFF)\n\
    \        y = y ^ (y << 5 & 0xFFFFFFFF)\n        return y & 0xFFFFFFFF\n    return\
    \ inner\n"
  dependsOn: []
  isVerificationFile: false
  path: misc/xorshift.py
  requiredBy:
  - DataStructure/Heap/RandomizedMeldableHeap.py
  timestamp: '2021-01-19 22:36:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: misc/xorshift.py
layout: document
title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
---
