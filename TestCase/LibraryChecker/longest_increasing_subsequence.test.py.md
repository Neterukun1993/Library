---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/lis.py
    title: "\u6700\u9577\u5897\u52A0\u90E8\u5206\u5217 (longest increasing subsequence)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/longest_increasing_subsequence
    links:
    - https://judge.yosupo.jp/problem/longest_increasing_subsequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence\n\
    import sys\ninput = sys.stdin.buffer.readline\n\n\nfrom DP.lis import lis_index\n\
    \n\ndef main():\n    n = int(input())\n    a = list(map(int, input().split()))\n\
    \n    result = lis_index(a, strict=True)\n\n    print(len(result))\n    print(*result)\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/lis.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/longest_increasing_subsequence.test.py
  requiredBy: []
  timestamp: '2023-03-03 23:23:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/longest_increasing_subsequence.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/longest_increasing_subsequence.test.py
- /verify/TestCase/LibraryChecker/longest_increasing_subsequence.test.py.html
title: TestCase/LibraryChecker/longest_increasing_subsequence.test.py
---
