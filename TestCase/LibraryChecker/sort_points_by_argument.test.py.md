---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Geometry/atan2_sorted.py
    title: "\u504F\u89D2\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sort_points_by_argument
    links:
    - https://judge.yosupo.jp/problem/sort_points_by_argument
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Geometry.atan2_sorted import\
    \ atan2_sorted\n\n\ndef main():\n    n = int(input())\n    coords = [list(map(int,\
    \ input().split())) for i in range(n)]\n\n    ans = atan2_sorted(coords)\n   \
    \ for res in ans:\n        print(*res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Geometry/atan2_sorted.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/sort_points_by_argument.test.py
  requiredBy: []
  timestamp: '2021-05-07 00:33:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/sort_points_by_argument.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/sort_points_by_argument.test.py
- /verify/TestCase/LibraryChecker/sort_points_by_argument.test.py.html
title: TestCase/LibraryChecker/sort_points_by_argument.test.py
---
