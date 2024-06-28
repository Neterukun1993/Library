---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/totient_sum.py
    title: "\u30AA\u30A4\u30E9\u30FC\u306E $\\varphi$ \u95A2\u6570\u306E\u548C"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_totient_function
    links:
    - https://judge.yosupo.jp/problem/sum_of_totient_function
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_totient_function\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.misc.totient_sum\
    \ import totient_sum\n\n\nMOD = 998244353\n\n\ndef main():\n    n = int(input())\n\
    \    print(totient_sum(n, MOD))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/misc/totient_sum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/sum_of_totient_function.test.py
  requiredBy: []
  timestamp: '2022-08-07 16:49:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/sum_of_totient_function.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/sum_of_totient_function.test.py
- /verify/TestCase/LibraryChecker/sum_of_totient_function.test.py.html
title: TestCase/LibraryChecker/sum_of_totient_function.test.py
---
