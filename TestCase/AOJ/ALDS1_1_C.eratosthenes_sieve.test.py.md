---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/eratosthenes_sieve.py
    title: "\u7D20\u6570\u5217\u6319 (\u30A8\u30E9\u30C8\u30B9\u30C6\u30CD\u30B9\u306E\
      \u7BE9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Prime.eratosthenes_sieve\
    \ import eratosthenes_sieve\n\n\ndef main():\n    n = int(input())\n    x = [int(input())\
    \ for i in range(n)]\n\n    _, prime_tbl = eratosthenes_sieve(max(x))\n    ans\
    \ = 0\n    for val in x:\n        if prime_tbl[val]:\n            ans += 1\n \
    \   print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Prime/eratosthenes_sieve.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
- /verify/TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py.html
title: TestCase/AOJ/ALDS1_1_C.eratosthenes_sieve.test.py
---
