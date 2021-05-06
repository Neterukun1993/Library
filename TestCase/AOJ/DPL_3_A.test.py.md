---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/largest_square_in_grid.py
    title: "\u30B0\u30EA\u30C3\u30C9\u4E2D\u306E\u6700\u5927\u6B63\u65B9\u5F62"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DP.largest_square_in_grid\
    \ import largest_square_in_grid\n\n\ndef main():\n    h, w = map(int, input().split())\n\
    \    c = [list(map(int, input().split())) for i in range(h)]\n\n    ans = largest_square_in_grid(c,\
    \ wall=1)\n    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/largest_square_in_grid.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_3_A.test.py
  requiredBy: []
  timestamp: '2021-05-07 05:41:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_3_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_3_A.test.py
- /verify/TestCase/AOJ/DPL_3_A.test.py.html
title: TestCase/AOJ/DPL_3_A.test.py
---
