---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/floor_sum.py
    title: floor sum
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.misc.floor_sum\
    \ import floor_sum\n\n\ndef main():\n    t = int(input())\n    for _ in range(t):\n\
    \        n, m, a, b = map(int, input().split())\n\n        ans = floor_sum(n,\
    \ m, a, b)\n        print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/misc/floor_sum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/sum_of_floor_of_linear.test.py
  requiredBy: []
  timestamp: '2021-05-03 22:51:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/sum_of_floor_of_linear.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/sum_of_floor_of_linear.test.py
- /verify/TestCase/LibraryChecker/sum_of_floor_of_linear.test.py.html
title: TestCase/LibraryChecker/sum_of_floor_of_linear.test.py
---
