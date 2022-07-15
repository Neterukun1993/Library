---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/dijkstra_trace.py
    title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O((E + V)\\log V)$) + \u7D4C\
      \u8DEF\u5FA9\u5143"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.ShortestPath.dijkstra_trace\
    \ import dijkstra, trace_route\n\n\ndef main():\n    n, m, s, t = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n    INF = 10\
    \ ** 18\n\n    graph = [[] for i in range(n)]\n    edge_idx = {}\n    for i, (u,\
    \ v, cost) in enumerate(edges):\n        graph[u].append((v, cost))\n\n    dist,\
    \ parent = dijkstra(s, graph)\n    path = trace_route(t, parent)\n\n    if not\
    \ path:\n        print(-1)\n    else:\n        es = []\n        for u, v in zip(path,\
    \ path[1:]):\n            es.append((u, v))\n        print(dist[t], len(es))\n\
    \        for res in es:\n            print(*res)\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/ShortestPath/dijkstra_trace.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/shortest_path.test.py
  requiredBy: []
  timestamp: '2022-01-22 18:47:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/shortest_path.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/shortest_path.test.py
- /verify/TestCase/LibraryChecker/shortest_path.test.py.html
title: TestCase/LibraryChecker/shortest_path.test.py
---
