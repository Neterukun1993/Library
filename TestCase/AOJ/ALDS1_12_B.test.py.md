---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/dijkstra_v2.py
    title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O(V^2)$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.ShortestPath.dijkstra_v2\
    \ import dijkstra_v2\n\n\ndef main():\n    n = int(input())\n    edges = [list(map(int,\
    \ input().split())) for i in range(n)]\n    INF = 10 ** 18\n\n    matrix = [[INF]\
    \ * n for i in range(n)]\n    for v in range(n):\n        matrix[v][v] = 0\n \
    \       for i in range(1, len(edges[v]) // 2):\n            nxt_v, cost = edges[v][slice(2\
    \ * i, 2 * (i + 1))]\n            matrix[v][nxt_v] = cost\n\n    dist = dijkstra_v2(0,\
    \ matrix)\n    for v, ans in enumerate(dist):\n        print(v, ans)\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/ShortestPath/dijkstra_v2.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_12_B.test.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_12_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_12_B.test.py
- /verify/TestCase/AOJ/ALDS1_12_B.test.py.html
title: TestCase/AOJ/ALDS1_12_B.test.py
---
