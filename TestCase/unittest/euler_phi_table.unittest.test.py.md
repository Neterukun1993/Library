---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/euler_phi.py
    title: "\u30AA\u30A4\u30E9\u30FC\u306E $\\varphi$ \u95A2\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.misc.euler_phi\
    \ import euler_phi_table\n\n\ndef test():\n    expected = [0, 1, 1, 2, 2, 4, 2,\
    \ 6, 4, 6, 4, 10, 4, 12, 6, 8]\n    n = len(expected) - 1\n\n    for i in range(n\
    \ + 1):\n        table = euler_phi_table(i)\n        assert table == expected[:i\
    \ + 1]\n\n\ndef main():\n    test()\n\n\nif __name__ == '__main__':\n    main()\n\
    \    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/misc/euler_phi.py
  isVerificationFile: true
  path: TestCase/unittest/euler_phi_table.unittest.test.py
  requiredBy: []
  timestamp: '2021-08-12 23:00:53+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/euler_phi_table.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/euler_phi_table.unittest.test.py
- /verify/TestCase/unittest/euler_phi_table.unittest.test.py.html
title: TestCase/unittest/euler_phi_table.unittest.test.py
---
