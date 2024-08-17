---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/matrix_rank_mod_2.test.py
    title: TestCase/LibraryChecker/matrix_rank_mod_2.test.py
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
  code: "def get_f2_basis(array):\n    base = []\n    for value in array:\n      \
    \  for e in base:\n            value = min(value, value ^ e)\n        if value\
    \ > 0:\n            base.append(value)\n    return base\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/get_f2_basis.py
  requiredBy: []
  timestamp: '2024-08-18 03:59:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/matrix_rank_mod_2.test.py
documentation_of: NumberTheory/ModularArithmetic/get_f2_basis.py
layout: document
redirect_from:
- /library/NumberTheory/ModularArithmetic/get_f2_basis.py
- /library/NumberTheory/ModularArithmetic/get_f2_basis.py.html
title: NumberTheory/ModularArithmetic/get_f2_basis.py
---
