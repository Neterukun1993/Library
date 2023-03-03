---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/zalgorithm.test.py
    title: TestCase/LibraryChecker/zalgorithm.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def z_algorithm(s):\n    res = [0] * len(s)\n    res[0] = len(s)\n    i,\
    \ j = 1, 0\n    while i < len(s):\n        while i + j < len(s) and s[j] == s[i\
    \ + j]:\n            j += 1\n        res[i] = j\n        if j == 0:\n        \
    \    i += 1\n            continue\n        k = 1\n        while i + k < len(s)\
    \ and k + res[k] < j:\n            res[i + k] = res[k]\n            k += 1\n \
    \       i, j = i + k, j - k\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: String/z_algorithm.py
  requiredBy: []
  timestamp: '2021-01-05 22:30:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/zalgorithm.test.py
documentation_of: String/z_algorithm.py
layout: document
title: Z algorithm
---
## 使い方
`z_algorithm(s: Sequence[Any]) -> List[int]`  
`s` と `s[i:]` の共通接頭辞の長さを格納した長さ `n = len(s)` の配列を返す。計算量 $O(n)$
