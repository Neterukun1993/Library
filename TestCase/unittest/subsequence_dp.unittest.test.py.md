---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/subsequence_dp.py
    title: "\u90E8\u5206\u5217 DP ($O(\\sigma N)$)"
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
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DP.subsequence_dp import\
    \ subsequence_dp\nfrom itertools import product\n\n\ndef bruteforce(small_characters,\
    \ MOD):\n    n = len(small_characters)\n    strs = set()\n\n    for bit_state\
    \ in range(1 << n):\n        tmp = \"\"\n        for i in range(n):\n        \
    \    if (bit_state >> i) & 1:\n                tmp += small_characters[i]\n  \
    \      strs.add(tmp)\n    return len(strs) % MOD\n\n\ndef main():\n    ALPH =\
    \ \"abcd\"\n    MOD = 10 ** 9 + 7\n\n    for rep in range(8):\n        for string\
    \ in product(ALPH, repeat=rep):\n            dp_sol = subsequence_dp(string, MOD)\n\
    \            bf_sol = bruteforce(string, MOD)\n            assert(dp_sol == bf_sol)\n\
    \n\nif __name__ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - DP/subsequence_dp.py
  isVerificationFile: true
  path: TestCase/unittest/subsequence_dp.unittest.test.py
  requiredBy: []
  timestamp: '2022-07-30 20:30:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/subsequence_dp.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/subsequence_dp.unittest.test.py
- /verify/TestCase/unittest/subsequence_dp.unittest.test.py.html
title: TestCase/unittest/subsequence_dp.unittest.test.py
---
