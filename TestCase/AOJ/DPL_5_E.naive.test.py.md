---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Combination.modinv_combination\
    \ import combination\n\n\ndef main():\n    n, k = map(int, input().split())\n\
    \    MOD = 10 ** 9 + 7\n    if n > k:\n        print(0)\n    else:\n        print(combination(k,\
    \ n, MOD))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Combination/modinv_combination.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_5_E.naive.test.py
  requiredBy: []
  timestamp: '2021-09-08 22:15:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_5_E.naive.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_5_E.naive.test.py
- /verify/TestCase/AOJ/DPL_5_E.naive.test.py.html
title: TestCase/AOJ/DPL_5_E.naive.test.py
---
