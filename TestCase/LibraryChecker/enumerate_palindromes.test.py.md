---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String/Manacher.py
    title: "\u6700\u9577\u56DE\u6587 (Manacher\u306E\u30A2\u30EB\u30B4\u30EA\u30BA\
      \u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_palindromes
    links:
    - https://judge.yosupo.jp/problem/enumerate_palindromes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes\n\
    import sys\ninput = sys.stdin.readline\n\nfrom String.Manacher import Manacher\n\
    \n\ndef main():\n    s = input().replace('\\n', '')\n    mn = Manacher(s)\n\n\
    \    print(*mn.len_p[1:-1])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - String/Manacher.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/enumerate_palindromes.test.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/enumerate_palindromes.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/enumerate_palindromes.test.py
- /verify/TestCase/LibraryChecker/enumerate_palindromes.test.py.html
title: TestCase/LibraryChecker/enumerate_palindromes.test.py
---
