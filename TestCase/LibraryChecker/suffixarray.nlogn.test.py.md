---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String/SA_nlogn.py
    title: "\u63A5\u5C3E\u8F9E\u914D\u5217 ($\\mathrm{O}(N (\\log N))$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/suffixarray
    links:
    - https://judge.yosupo.jp/problem/suffixarray
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray\n\
    import sys\ninput = sys.stdin.readline\n\nfrom String.SA_nlogn import SuffixArray\n\
    \n\ndef main():\n    s = input().replace('\\n', '')\n    sa = SuffixArray(s)\n\
    \n    print(*sa.sa[1:])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - String/SA_nlogn.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/suffixarray.nlogn.test.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/suffixarray.nlogn.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/suffixarray.nlogn.test.py
- /verify/TestCase/LibraryChecker/suffixarray.nlogn.test.py.html
title: TestCase/LibraryChecker/suffixarray.nlogn.test.py
---
