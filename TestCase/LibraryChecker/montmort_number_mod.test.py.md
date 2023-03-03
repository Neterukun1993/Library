---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/montmort_number.py
    title: "\u30E2\u30F3\u30E2\u30FC\u30EB\u6570 (\u5B8C\u5168\u9806\u5217)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/montmort_number_mod
    links:
    - https://judge.yosupo.jp/problem/montmort_number_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Combination.montmort_number\
    \ import montmort_number, montmort_number2\n\n\ndef main():\n    n, m = map(int,\
    \ input().split())\n\n    res = montmort_number(n, m)\n    res2 = montmort_number2(n,\
    \ m)\n    assert(res == res2)\n    print(*res[1:])\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Combination/montmort_number.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/montmort_number_mod.test.py
  requiredBy: []
  timestamp: '2021-01-27 22:05:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/montmort_number_mod.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/montmort_number_mod.test.py
- /verify/TestCase/LibraryChecker/montmort_number_mod.test.py.html
title: TestCase/LibraryChecker/montmort_number_mod.test.py
---
