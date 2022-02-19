---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/gcd_lcm.py
    title: "\u6700\u5927\u516C\u7D04\u6570\u3068\u6700\u5C0F\u516C\u500D\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Basic.gcd_lcm\
    \ import gcd\n\n\ndef main():\n    x, y = map(int, input().split())\n    print(gcd(x,\
    \ y))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Basic/gcd_lcm.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_1_B.test.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_1_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_1_B.test.py
- /verify/TestCase/AOJ/ALDS1_1_B.test.py.html
title: TestCase/AOJ/ALDS1_1_B.test.py
---
