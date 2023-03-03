---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/ntt_convolve.py
    title: "\u6570\u8AD6\u5909\u63DB (number-theoretic transform)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/convolution_mod
    links:
    - https://judge.yosupo.jp/problem/convolution_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.ntt_convolve\
    \ import ntt_convolve\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    b = list(map(int, input().split()))\n\
    \n    print(*ntt_convolve(a, b))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/Convolution/ntt_convolve.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/convolution_mod.test.py
  requiredBy: []
  timestamp: '2021-06-13 01:12:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/convolution_mod.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/convolution_mod.test.py
- /verify/TestCase/LibraryChecker/convolution_mod.test.py.html
title: TestCase/LibraryChecker/convolution_mod.test.py
---
