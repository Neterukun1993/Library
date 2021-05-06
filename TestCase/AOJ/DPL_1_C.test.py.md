---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/knapsack_unbounded.py
    title: "\u500B\u6570\u5236\u9650\u306A\u3057\u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\
      \u554F\u984C"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DP.knapsack_unbounded import\
    \ knapsack_unbounded\n\n\ndef main():\n    n, w = map(int, input().split())\n\
    \    items = [list(map(int, input().split())) for i in range(n)]\n\n    ans =\
    \ knapsack_unbounded(w, items)\n    print(ans)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DP/knapsack_unbounded.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_1_C.test.py
  requiredBy: []
  timestamp: '2021-05-04 20:55:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_1_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_1_C.test.py
- /verify/TestCase/AOJ/DPL_1_C.test.py.html
title: TestCase/AOJ/DPL_1_C.test.py
---