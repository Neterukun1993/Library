---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/extended_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Basic.extended_gcd\
    \ import extended_gcd\n\n\ndef main():\n    a, b = map(int, input().split())\n\
    \n    _, x, y = extended_gcd(a, b)\n    print(x, y)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - NumberTheory/Basic/extended_gcd.py
  isVerificationFile: true
  path: TestCase/AOJ/NTL_1_E.test.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/NTL_1_E.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/NTL_1_E.test.py
- /verify/TestCase/AOJ/NTL_1_E.test.py.html
title: TestCase/AOJ/NTL_1_E.test.py
---
