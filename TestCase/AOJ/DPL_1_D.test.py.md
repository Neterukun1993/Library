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
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D\n\
    import sys\ninput = sys.stdin.readline\n\nfrom DP.lis import lis\n\n\ndef main():\n\
    \    n = int(input())\n    a = [int(input()) for i in range(n)]\n\n    ans = len(lis(a))\n\
    \    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/lis.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_1_D.test.py
  requiredBy: []
  timestamp: '2021-05-06 13:26:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_1_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_1_D.test.py
- /verify/TestCase/AOJ/DPL_1_D.test.py.html
title: TestCase/AOJ/DPL_1_D.test.py
---
