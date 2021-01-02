---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/twelvefold_way.py
    title: Combination/twelvefold_way.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_I
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_I
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_I\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Combination.twelvefold_way import\
    \ way9\n\n\ndef main():\n    n, k = map(int, input().split())\n    print(way9(n,\
    \ k))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Combination/twelvefold_way.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_5_I.test.py
  requiredBy: []
  timestamp: '2021-01-02 20:38:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_5_I.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_5_I.test.py
- /verify/TestCase/AOJ/DPL_5_I.test.py.html
title: TestCase/AOJ/DPL_5_I.test.py
---
