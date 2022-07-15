---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/prime_factors.py
    title: "\u7D20\u56E0\u6570\u5206\u89E3 (\u8A66\u3057\u5272\u308A\u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Prime.prime_factors\
    \ import prime_factors, prime_factors_distinct, prime_factors_compress\n\n\ndef\
    \ main():\n    n = int(input())\n\n    pf = prime_factors(n)\n    pf_distinct\
    \ = prime_factors_distinct(n)\n    pf_compress = prime_factors_compress(n)\n\n\
    \    assert(sorted(set(pf)) == pf_distinct)\n    pf_test = []\n    for val, cnt\
    \ in pf_compress:\n        for _ in range(cnt):\n            pf_test.append(val)\n\
    \    assert(pf_test == pf)\n\n    print(f'{n}: {\" \".join(map(str, pf))}')\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Prime/prime_factors.py
  isVerificationFile: true
  path: TestCase/AOJ/NTL_1_A.test.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/NTL_1_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/NTL_1_A.test.py
- /verify/TestCase/AOJ/NTL_1_A.test.py.html
title: TestCase/AOJ/NTL_1_A.test.py
---
