---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/is_prime.py
    title: "\u7D20\u6570\u5224\u5B9A (\u8A66\u3057\u5272\u308A\u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Prime.is_prime\
    \ import is_prime\n\n\ndef main():\n    n = int(input())\n    x = [int(input())\
    \ for i in range(n)]\n\n    ans = 0\n    for val in x:\n        if is_prime(val):\n\
    \            ans += 1\n    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Prime/is_prime.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_1_C.test.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_1_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_1_C.test.py
- /verify/TestCase/AOJ/ALDS1_1_C.test.py.html
title: TestCase/AOJ/ALDS1_1_C.test.py
---
