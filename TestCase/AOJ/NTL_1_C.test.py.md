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
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Basic.gcd_lcm\
    \ import lcm, all_lcm_int, all_lcm_dict\n\n\ndef main():\n    n = int(input())\n\
    \    a = list(map(int, input().split()))\n\n    lcm0 = 1\n    for val in a:\n\
    \        lcm0 = lcm(lcm0, val)\n\n    lcm1 = all_lcm_int(a)\n\n    factors = all_lcm_dict(a)\n\
    \    lcm2 = 1\n    for val in factors:\n        lcm2 *= val ** factors[val]\n\n\
    \    assert(lcm0 == lcm1 and lcm1 == lcm2)\n    print(lcm0)\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Basic/gcd_lcm.py
  isVerificationFile: true
  path: TestCase/AOJ/NTL_1_C.test.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/NTL_1_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/NTL_1_C.test.py
- /verify/TestCase/AOJ/NTL_1_C.test.py.html
title: TestCase/AOJ/NTL_1_C.test.py
---
