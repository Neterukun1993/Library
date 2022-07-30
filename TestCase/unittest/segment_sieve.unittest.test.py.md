---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/miller_rabin.py
    title: "\u78BA\u7387\u7684\u7D20\u6570\u5224\u5B9A (\u30DF\u30E9\u30FC\u30FB\u30E9\
      \u30D3\u30F3\u7D20\u6570\u5224\u5B9A\u6CD5)"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Prime/segment_sieve.py
    title: "\u7D20\u6570\u5217\u6319 (\u533A\u9593\u7BE9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Prime.segment_sieve\
    \ import segment_sieve\nfrom NumberTheory.Prime.miller_rabin import miller_rabin\n\
    \n\ndef main():\n    length = 10 ** 5\n    for l in range(10 ** 9, 10 ** 9 + 10):\n\
    \        prime_list, prime_table = segment_sieve(l, l + length)\n        idx =\
    \ 0\n        for i, is_prime in enumerate(prime_table):\n            val = l +\
    \ i\n            assert(is_prime == miller_rabin(val))\n            if is_prime:\n\
    \                assert(prime_list[idx] == val)\n                idx += 1\n\n\n\
    if __name__ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/Prime/miller_rabin.py
  - NumberTheory/Prime/segment_sieve.py
  isVerificationFile: true
  path: TestCase/unittest/segment_sieve.unittest.test.py
  requiredBy: []
  timestamp: '2021-03-05 16:39:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/segment_sieve.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/segment_sieve.unittest.test.py
- /verify/TestCase/unittest/segment_sieve.unittest.test.py.html
title: TestCase/unittest/segment_sieve.unittest.test.py
---
