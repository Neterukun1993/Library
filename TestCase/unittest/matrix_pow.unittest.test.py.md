---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/matrix_pow.py
    title: "\u884C\u5217\u7D2F\u4E57"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.misc.matrix_pow\
    \ import matrix_pow, matvec_mul\n\n\nMOD = 10 ** 9 + 7\nn = 10 ** 4\n\n\nfib =\
    \ [0] * (n + 1)\nfib[1] = 1\nfor i in range(n - 1):\n    fib[i + 2] = fib[i +\
    \ 1] + fib[i]\n    fib[i + 1] %= MOD\n\n\ndef fib_matrix_pow(k):\n    mat = [[1,\
    \ 1], [1, 0]]\n    matpow = matrix_pow(mat, k, MOD)\n    vec = matvec_mul(matpow,\
    \ [1, 0], MOD)\n    return vec[1]\n\n\ndef main():\n    for i in range(n):\n \
    \       assert(fib[i] == fib_matrix_pow(i))\n\n\nif __name__ == '__main__':\n\
    \    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/misc/matrix_pow.py
  isVerificationFile: true
  path: TestCase/unittest/matrix_pow.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-12 19:23:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/matrix_pow.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/matrix_pow.unittest.test.py
- /verify/TestCase/unittest/matrix_pow.unittest.test.py.html
title: TestCase/unittest/matrix_pow.unittest.test.py
---
