---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: NumberTheory/misc/matrix_pow.py
    title: "\u884C\u5217\u7D2F\u4E57"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
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
  isVerificationFile: false
  path: TestCase/unittest/matrix_pow.unittest.py
  requiredBy: []
  timestamp: '2021-06-07 19:35:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: TestCase/unittest/matrix_pow.unittest.py
layout: document
redirect_from:
- /library/TestCase/unittest/matrix_pow.unittest.py
- /library/TestCase/unittest/matrix_pow.unittest.py.html
title: TestCase/unittest/matrix_pow.unittest.py
---
