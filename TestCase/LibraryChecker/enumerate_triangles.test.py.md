---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/enumerate_triangles.py
    title: "\u4E09\u89D2\u5F62\u306E\u6570\u3048\u4E0A\u3052"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_triangles
    links:
    - https://judge.yosupo.jp/problem/enumerate_triangles
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_triangles\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.enumerate_triangles\
    \ import enumerate_triangles\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    x = list(map(int, input().split()))\n    edges = [list(map(int, input().split()))\
    \ for i in range(m)]\n    MOD = 998244353\n\n    _, ans = enumerate_triangles(edges,\
    \ x, MOD)\n    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/enumerate_triangles.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/enumerate_triangles.test.py
  requiredBy: []
  timestamp: '2021-01-21 18:47:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/enumerate_triangles.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/enumerate_triangles.test.py
- /verify/TestCase/LibraryChecker/enumerate_triangles.test.py.html
title: TestCase/LibraryChecker/enumerate_triangles.test.py
---
