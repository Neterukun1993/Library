---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Geometry/closest_pair.py
    title: "\u6700\u8FD1\u70B9\u5BFE"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_5_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Geometry.closest_pair import\
    \ closest_pair\n\n\ndef main():\n    n = int(input())\n    points = [list(map(float,\
    \ input().split())) for i in range(n)]\n\n    print('{:.10f}'.format(closest_pair(points)))\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Geometry/closest_pair.py
  isVerificationFile: true
  path: TestCase/AOJ/CGL_5_A.test.py
  requiredBy: []
  timestamp: '2021-02-07 13:29:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/CGL_5_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/CGL_5_A.test.py
- /verify/TestCase/AOJ/CGL_5_A.test.py.html
title: TestCase/AOJ/CGL_5_A.test.py
---
