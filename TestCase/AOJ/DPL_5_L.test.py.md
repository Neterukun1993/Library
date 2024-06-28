---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/twelvefold_way.py
    title: "\u5199\u50CF12\u76F8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_L
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_L
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_L\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Combination.twelvefold_way import\
    \ way12\n\n\ndef main():\n    n, k = map(int, input().split())\n    print(way12(n,\
    \ k))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Combination/twelvefold_way.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_5_L.test.py
  requiredBy: []
  timestamp: '2021-09-08 22:15:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_5_L.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_5_L.test.py
- /verify/TestCase/AOJ/DPL_5_L.test.py.html
title: TestCase/AOJ/DPL_5_L.test.py
---
