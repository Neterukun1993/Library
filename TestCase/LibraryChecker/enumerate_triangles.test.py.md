---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\misc\enumerate_triangles.py
    title: Graph\misc\enumerate_triangles.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_triangles
    links:
    - https://judge.yosupo.jp/problem/enumerate_triangles
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_triangles\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.misc.enumerate_triangles\
    \ import enumerate_triangles\r\n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\
    \n    x = list(map(int, input().split()))\r\n    edges = [list(map(int, input().split()))\
    \ for i in range(m)]\r\n    MOD = 998244353\r\n\r\n    _, ans = enumerate_triangles(edges,\
    \ x, MOD)\r\n    print(ans)\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\
    \n"
  dependsOn:
  - Graph\misc\enumerate_triangles.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\enumerate_triangles.test.py
  requiredBy: []
  timestamp: '2021-01-21 18:47:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\enumerate_triangles.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\enumerate_triangles.test.py
- /verify\TestCase\LibraryChecker\enumerate_triangles.test.py.html
title: TestCase\LibraryChecker\enumerate_triangles.test.py
---
