---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/largest_rectangle_in_histogram.py
    title: "\u30D2\u30B9\u30C8\u30B0\u30E9\u30E0\u4E2D\u306E\u6700\u5927\u9577\u65B9\
      \u5F62"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DP.largest_rectangle_in_histogram\
    \ import largest_rectangle_in_histogram\n\n\ndef main():\n    n = int(input())\n\
    \    h = list(map(int, input().split()))\n\n    ans = largest_rectangle_in_histogram(h)\n\
    \    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/largest_rectangle_in_histogram.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_3_C.test.py
  requiredBy: []
  timestamp: '2021-05-07 04:49:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_3_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_3_C.test.py
- /verify/TestCase/AOJ/DPL_3_C.test.py.html
title: TestCase/AOJ/DPL_3_C.test.py
---
