---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/linear_congruence.py
    title: "\u4E00\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.ModularArithmetic.linear_congruence\
    \ import linear_congruence\n\n\ndef test(a, b, m):\n    _, ans, _ = linear_congruence(a,\
    \ b, m)\n\n    res = -1\n    for i in range(m):\n        if a * i % m == b % m:\n\
    \            res = i\n            break\n    assert(ans == res)\n\n\ndef main():\n\
    \    # ax = b (mod m)\n    for a in range(50):\n        for b in range(50):\n\
    \            for m in range(1, 50):\n                test(a, b, m)\n\n\nif __name__\
    \ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/ModularArithmetic/linear_congruence.py
  isVerificationFile: true
  path: TestCase/unittest/linear_congruence.unittest.test.py
  requiredBy: []
  timestamp: '2021-05-07 02:19:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/linear_congruence.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/linear_congruence.unittest.test.py
- /verify/TestCase/unittest/linear_congruence.unittest.test.py.html
title: TestCase/unittest/linear_congruence.unittest.test.py
---
