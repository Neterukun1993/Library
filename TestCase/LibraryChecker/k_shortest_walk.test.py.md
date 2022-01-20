---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Graph/misc/k_shortest_walk.py
    title: "\u4E0A\u4F4D $k$ \u500B\u306E\u30A6\u30A9\u30FC\u30AF"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/k_shortest_walk
    links:
    - https://judge.yosupo.jp/problem/k_shortest_walk
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/k_shortest_walk\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.k_shortest_walk\
    \ import k_shortest_walk\n\n\ndef main():\n    n, m, start, goal, k = map(int,\
    \ input().split())\n    edges = [list(map(int, input().split())) for _ in range(m)]\n\
    \n    ans = k_shortest_walk(n, edges, start, goal, k)\n    for res in ans:\n \
    \       print(res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/k_shortest_walk.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/k_shortest_walk.test.py
  requiredBy: []
  timestamp: '2022-01-20 20:07:10+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/k_shortest_walk.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/k_shortest_walk.test.py
- /verify/TestCase/LibraryChecker/k_shortest_walk.test.py.html
title: TestCase/LibraryChecker/k_shortest_walk.test.py
---
