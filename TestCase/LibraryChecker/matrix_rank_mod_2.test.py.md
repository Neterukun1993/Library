---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/get_f2_basis.py
    title: NumberTheory/ModularArithmetic/get_f2_basis.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_rank_mod_2
    links:
    - https://judge.yosupo.jp/problem/matrix_rank_mod_2
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank_mod_2\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.ModularArithmetic.get_f2_basis\
    \ import get_f2_basis\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    if m == 0:\n        a = [0 for _ in range(n)]\n    else:\n        a = [int(input(),\
    \ 2) for _ in range(n)]\n\n    base = get_f2_basis(a)\n    print(len(base))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/ModularArithmetic/get_f2_basis.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/matrix_rank_mod_2.test.py
  requiredBy: []
  timestamp: '2024-08-18 03:59:59+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/matrix_rank_mod_2.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/matrix_rank_mod_2.test.py
- /verify/TestCase/LibraryChecker/matrix_rank_mod_2.test.py.html
title: TestCase/LibraryChecker/matrix_rank_mod_2.test.py
---
