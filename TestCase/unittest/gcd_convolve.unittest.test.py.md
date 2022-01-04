---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/gcd_convolve.py
    title: "\u6DFB\u5B57 gcd \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.gcd_convolve\
    \ import gcd_convolve\n\n\ndef naive_gcd_convolve(a, b):\n    \"\"\"O(N^2) naive\
    \ calculation\"\"\"\n    def gcd(x, y):\n        while y:\n            x, y =\
    \ y, x % y\n        return x\n\n    n = min(len(a), len(b))\n    res = [0] * n\n\
    \    for i, va in enumerate(a[1:], 1):\n        for j, vb in enumerate(b[1:],\
    \ 1):\n            res[gcd(i, j)] += va * vb\n    return res\n\n\ndef main():\n\
    \    n = 1000\n    a = [1] * n\n    b = [1] * n\n    a[0] = 0\n    b[0] = 0\n\
    \    assert(gcd_convolve(a, b) == naive_gcd_convolve(a, b))\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/Convolution/gcd_convolve.py
  isVerificationFile: true
  path: TestCase/unittest/gcd_convolve.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-24 01:16:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/gcd_convolve.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/gcd_convolve.unittest.test.py
- /verify/TestCase/unittest/gcd_convolve.unittest.test.py.html
title: TestCase/unittest/gcd_convolve.unittest.test.py
---
