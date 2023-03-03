---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/arithmetic_sequence.py
    title: "\u7B49\u5DEE\u6570\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Basic.arithmetic_sequence\
    \ import Arithmetic\n\n\ndef naive_sum(a0, d, r):\n    result = 0\n    for i in\
    \ range(r):\n        result += a0 + i * d\n    return result\n\n\ndef naive_range_sum(a0,\
    \ d, l, r):\n    result = 0\n    for i in range(l, r):\n        result += a0 +\
    \ i * d\n    return result\n\n\ndef main():\n    for a0 in range(-10, 10):\n \
    \       for d in range(-10, 10):\n            for r in range(10):\n          \
    \      assert(Arithmetic.sum(a0, d, r) == naive_sum(a0, d, r))\n\n    for a0 in\
    \ range(-10, 10):\n        for d in range(-10, 10):\n            for l in range(10):\n\
    \                for r in range(l, r):\n                    assert(Arithmetic.range_sum(a0,\
    \ d, l, r)\n                           == naive_range_sum(a0, d, l, r))\n\nif\
    \ __name__ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/Basic/arithmetic_sequence.py
  isVerificationFile: true
  path: TestCase/unittest/arithmetic_sequence.unittest.test.py
  requiredBy: []
  timestamp: '2022-01-21 18:13:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/arithmetic_sequence.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/arithmetic_sequence.unittest.test.py
- /verify/TestCase/unittest/arithmetic_sequence.unittest.test.py.html
title: TestCase/unittest/arithmetic_sequence.unittest.test.py
---
