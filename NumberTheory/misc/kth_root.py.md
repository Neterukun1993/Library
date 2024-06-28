---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/kth_root_integer.test.py
    title: TestCase/LibraryChecker/kth_root_integer.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def kth_root(a, k):\n    res = int(pow(a, 1 / k))\n    while pow(res + 1,\
    \ k) <= a:\n        res += 1\n    while pow(res, k) > a:\n        res -= 1\n \
    \   return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/misc/kth_root.py
  requiredBy: []
  timestamp: '2022-01-19 23:55:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/kth_root_integer.test.py
documentation_of: NumberTheory/misc/kth_root.py
layout: document
title: kth_root
---

## 使い方
`kth_root(a: int, k: int) -> int:`  
$\mathrm{floor} (a ^ {1/k})$ を返す。
