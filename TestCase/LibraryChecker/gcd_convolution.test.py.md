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
    PROBLEM: https://judge.yosupo.jp/problem/gcd_convolution
    links:
    - https://judge.yosupo.jp/problem/gcd_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_convolution\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.gcd_convolve\
    \ import gcd_convolve\n\n\ndef main():\n    n = int(input())\n    a = list(map(int,\
    \ input().split()))\n    b = list(map(int, input().split()))\n\n    print(*gcd_convolve([0]\
    \ + a, [0] + b)[1:])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Convolution/gcd_convolve.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/gcd_convolution.test.py
  requiredBy: []
  timestamp: '2022-07-31 17:54:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/gcd_convolution.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/gcd_convolution.test.py
- /verify/TestCase/LibraryChecker/gcd_convolution.test.py.html
title: TestCase/LibraryChecker/gcd_convolution.test.py
---
