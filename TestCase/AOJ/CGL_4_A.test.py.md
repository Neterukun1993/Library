---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Geometry/convexhull.py
    title: "\u51F8\u5305"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Geometry.convexhull import\
    \ convexhull\n\n\ndef main():\n    n = int(input())\n    points = [list(map(int,\
    \ input().split())) for i in range(n)]\n\n    ch = convexhull(points)\n    x,\
    \ y = 10 ** 8, 10 ** 8\n    minidx = 0\n    for i in range(len(ch)):\n       \
    \ if ch[i][1] < y or (ch[i][1] == y and ch[i][0] < x):\n            minidx = i\n\
    \            x, y = ch[i]\n    ch = ch[minidx:] + ch[:minidx]\n\n    print(len(ch))\n\
    \    for res in ch:\n        print(*res)\n\n\nif __name__ == '__main__':\n   \
    \ main()\n"
  dependsOn:
  - Geometry/convexhull.py
  isVerificationFile: true
  path: TestCase/AOJ/CGL_4_A.test.py
  requiredBy: []
  timestamp: '2021-05-17 22:33:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/CGL_4_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/CGL_4_A.test.py
- /verify/TestCase/AOJ/CGL_4_A.test.py.html
title: TestCase/AOJ/CGL_4_A.test.py
---
