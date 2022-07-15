---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/misc/kth_root.py
    title: kth_root
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/kth_root_integer
    links:
    - https://judge.yosupo.jp/problem/kth_root_integer
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_root_integer\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.misc.kth_root\
    \ import kth_root\n\n\ndef main():\n    t = int(input())\n\n    for _ in range(t):\n\
    \        a, k = map(int, input().split())\n        print(kth_root(a, k))\n\n\n\
    if __name__ == '__main__':\n    main()\n"
  dependsOn:
  - NumberTheory/misc/kth_root.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/kth_root_integer.test.py
  requiredBy: []
  timestamp: '2022-01-19 23:55:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/kth_root_integer.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/kth_root_integer.test.py
- /verify/TestCase/LibraryChecker/kth_root_integer.test.py.html
title: TestCase/LibraryChecker/kth_root_integer.test.py
---
