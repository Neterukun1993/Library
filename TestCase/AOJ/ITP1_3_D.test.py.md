---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/divisors.py
    title: "\u7D04\u6570\u5217\u6319 (\u8A66\u3057\u5272\u308A\u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Prime.divisors\
    \ import divisors\n\n\ndef main():\n    a, b, c = map(int, input().split())\n\n\
    \    divs = divisors(c)\n    ans = 0\n    for val in divs:\n        ans += (a\
    \ <= val <= b)\n\n    print(ans)\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Prime/divisors.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP1_3_D.test.py
  requiredBy: []
  timestamp: '2021-04-30 21:12:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP1_3_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP1_3_D.test.py
- /verify/TestCase/AOJ/ITP1_3_D.test.py.html
title: TestCase/AOJ/ITP1_3_D.test.py
---
