---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/linear_equations.py
    title: "\u9023\u7ACB\u4E00\u6B21\u65B9\u7A0B\u5F0F"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/system_of_linear_equations
    links:
    - https://judge.yosupo.jp/problem/system_of_linear_equations
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.ModularArithmetic.linear_equations\
    \ import linear_equations\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    a = [list(map(int, input().split())) for _ in range(n)]\n    b = list(map(int,\
    \ input().split()))\n\n    dimension, result, basis_vectors = linear_equations(a,\
    \ b)\n    print(dimension)\n    print(*result)\n    for vector in basis_vectors:\n\
    \        print(*vector)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/ModularArithmetic/linear_equations.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/system_of_linear_equations.test.py
  requiredBy: []
  timestamp: '2024-08-18 03:37:20+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/system_of_linear_equations.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/system_of_linear_equations.test.py
- /verify/TestCase/LibraryChecker/system_of_linear_equations.test.py.html
title: TestCase/LibraryChecker/system_of_linear_equations.test.py
---
