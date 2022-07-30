---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/count_subsequence.py
    title: "\u90E8\u5206\u5217 DP ($O(N)$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/number_of_subsequences
    links:
    - https://judge.yosupo.jp/problem/number_of_subsequences
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DP.count_subsequence import\
    \ count_subsequence\n\n\ndef main():\n    n = int(input())\n    a = list(map(int,\
    \ input().split()))\n\n    MOD = 998244353\n\n    res = (count_subsequence(a,\
    \ MOD) - 1) % MOD\n    print(res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/count_subsequence.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/number_of_subsequences.test.py
  requiredBy: []
  timestamp: '2022-07-30 20:30:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/number_of_subsequences.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/number_of_subsequences.test.py
- /verify/TestCase/LibraryChecker/number_of_subsequences.test.py.html
title: TestCase/LibraryChecker/number_of_subsequences.test.py
---
