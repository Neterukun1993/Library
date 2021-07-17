---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/xor_convolve.py
    title: "\u6DFB\u5B57 xor \u306B\u3088\u308B\u7573\u307F\u8FBC\u307F"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.xor_convolve\
    \ import xor_convolve\n\n\ndef main():\n    n = int(input())\n    a = list(map(int,\
    \ input().split()))\n    b = list(map(int, input().split()))\n\n    print(*xor_convolve(a,\
    \ b))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Convolution/xor_convolve.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/bitwise_xor_convolution.test.py
  requiredBy: []
  timestamp: '2021-06-21 01:35:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/bitwise_xor_convolution.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/bitwise_xor_convolution.test.py
- /verify/TestCase/LibraryChecker/bitwise_xor_convolution.test.py.html
title: TestCase/LibraryChecker/bitwise_xor_convolution.test.py
---
