---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/dijkstra.py
    title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O((E + V)\\log V)$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.ShortestPath.dijkstra import\
    \ dijkstra\n\n\ndef main():\n    n, m, s = map(int, input().split())\n    edges\
    \ = [list(map(int, input().split())) for i in range(m)]\n    INF = 10 ** 18\n\n\
    \    graph = [[] for i in range(n)]\n    for u, v, cost in edges:\n        graph[u].append((v,\
    \ cost))\n\n    dist = dijkstra(s, graph)\n    for val in dist:\n        if val\
    \ == INF:\n            print(\"INF\")\n        else:\n            print(val)\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/ShortestPath/dijkstra.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_1_A.test.py
  requiredBy: []
  timestamp: '2022-01-22 12:11:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_1_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_1_A.test.py
- /verify/TestCase/AOJ/GRL_1_A.test.py.html
title: TestCase/AOJ/GRL_1_A.test.py
---
