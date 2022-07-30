---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/RandomizedMeldableHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Randomized Meldable Heap)"
  - icon: ':heavy_check_mark:'
    path: DataStructure/List/SkipList.py
    title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\
      /\u633F\u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (\u30B9\u30AD\u30C3\
      \u30D7\u30EA\u30B9\u30C8)"
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedSetSkipList.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (\u30B9\u30AD\u30C3\u30D7\u30EA\u30B9\
      \u30C8)"
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedSetTreap.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (Treap)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/IntervalHeap.unittest.test.py
    title: TestCase/unittest/IntervalHeap.unittest.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/LazyBinaryTrie.unittest.test.py
    title: TestCase/unittest/LazyBinaryTrie.unittest.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
    title: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/xorshift.unittest.test.py
    title: TestCase/unittest/xorshift.unittest.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/zeta_mobius_transform.unittest.test.py
    title: TestCase/unittest/zeta_mobius_transform.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def xorshift32():\n    y = 2463534242\n    def inner():\n        nonlocal\
    \ y\n        y = y ^ (y << 13 & 0xFFFFFFFF)\n        y = y ^ (y >> 17 & 0xFFFFFFFF)\n\
    \        y = y ^ (y << 5 & 0xFFFFFFFF)\n        return y & 0xFFFFFFFF\n    return\
    \ inner\n"
  dependsOn: []
  isVerificationFile: false
  path: misc/xorshift.py
  requiredBy:
  - DataStructure/List/SkipList.py
  - DataStructure/Heap/RandomizedMeldableHeap.py
  - DataStructure/SortedSet/SortedSetSkipList.py
  - DataStructure/SortedSet/SortedSetTreap.py
  timestamp: '2021-01-19 22:36:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/xorshift.unittest.test.py
  - TestCase/unittest/LazyBinaryTrie.unittest.test.py
  - TestCase/unittest/zeta_mobius_transform.unittest.test.py
  - TestCase/unittest/IntervalHeap.unittest.test.py
  - TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
documentation_of: misc/xorshift.py
layout: document
title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
---
