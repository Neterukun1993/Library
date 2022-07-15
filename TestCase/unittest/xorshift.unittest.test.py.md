---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
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
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom misc.xorshift import xorshift32\n\
    \n\ndef main():\n    sample = [\n        723471715,\n        2497366906,\n   \
    \     2064144800,\n        2008045182,\n        3532304609,\n        374114282,\n\
    \        1350636274,\n        691148861,\n        746858951,\n        2653896249\n\
    \    ]\n\n    for _ in range(2):\n        xor32 = xorshift32()\n        for val\
    \ in sample:\n            assert(val == xor32())\n\n\nif __name__ == '__main__':\n\
    \    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - misc/xorshift.py
  isVerificationFile: true
  path: TestCase/unittest/xorshift.unittest.test.py
  requiredBy: []
  timestamp: '2021-05-07 19:18:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/xorshift.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/xorshift.unittest.test.py
- /verify/TestCase/unittest/xorshift.unittest.test.py.html
title: TestCase/unittest/xorshift.unittest.test.py
---
