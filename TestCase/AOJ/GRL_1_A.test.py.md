---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\ShortestPath\dijkstra.py
    title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.ShortestPath.dijkstra\
    \ import dijkstra\r\n\r\n\r\ndef main():\r\n    n, m, s = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for i in range(m)]\r\n    INF =\
    \ 10 ** 18\r\n\r\n    graph = [[] for i in range(n)]\r\n    for u, v, cost in\
    \ edges:\r\n        graph[u].append((v, cost))\r\n\r\n    dist = dijkstra(s, graph)\r\
    \n    for val in dist:\r\n        if val == INF:\r\n            print(\"INF\"\
    )\r\n        else:\r\n            print(val)\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - Graph\ShortestPath\dijkstra.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_1_A.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_1_A.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_1_A.test.py
- /verify\TestCase\AOJ\GRL_1_A.test.py.html
title: TestCase\AOJ\GRL_1_A.test.py
---
