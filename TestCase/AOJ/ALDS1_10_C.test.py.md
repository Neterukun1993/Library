---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/lcs.py
    title: "\u6700\u9577\u5171\u901A\u90E8\u5206\u5217 (longest common subsequence)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C\n\
    from DP.lcs import lcs\n\n\ndef main():\n    q = int(input())\n    for _ in range(q):\n\
    \        x = input()\n        y = input()\n\n        print(len(lcs(x, y)))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DP/lcs.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_10_C.test.py
  requiredBy: []
  timestamp: '2021-05-06 21:57:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_10_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_10_C.test.py
- /verify/TestCase/AOJ/ALDS1_10_C.test.py.html
title: TestCase/AOJ/ALDS1_10_C.test.py
---
