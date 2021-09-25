---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/euler_phi.py
    title: "\u30AA\u30A4\u30E9\u30FC\u306E $\\varphi$ \u95A2\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D\n\
    import sys\ninput = sys.stdin.readline\n\nfrom NumberTheory.misc.euler_phi import\
    \ euler_phi\n\n\ndef main():\n    n = int(input())\n    print(euler_phi(n))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/misc/euler_phi.py
  isVerificationFile: true
  path: TestCase/AOJ/NTL_1_D.test.py
  requiredBy: []
  timestamp: '2021-08-12 23:00:53+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/NTL_1_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/NTL_1_D.test.py
- /verify/TestCase/AOJ/NTL_1_D.test.py.html
title: TestCase/AOJ/NTL_1_D.test.py
---
