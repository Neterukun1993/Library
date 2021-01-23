---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\ShortestPath\dijkstra_v2.py
    title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($\\mathrm{O}(V^2)$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.ShortestPath.dijkstra_v2\
    \ import dijkstra_v2\r\n\r\n\r\ndef main():\r\n    n = int(input())\r\n    edges\
    \ = [list(map(int, input().split())) for i in range(n)]\r\n    INF = 10 ** 18\r\
    \n\r\n    matrix = [[INF] * n for i in range(n)]\r\n    for v in range(n):\r\n\
    \        matrix[v][v] = 0\r\n        for i in range(1, len(edges[v]) // 2):\r\n\
    \            nxt_v, cost = edges[v][slice(2 * i, 2 * (i + 1))]\r\n           \
    \ matrix[v][nxt_v] = cost\r\n\r\n    dist = dijkstra_v2(0, matrix)\r\n    for\
    \ v, ans in enumerate(dist):\r\n        print(v, ans)\r\n\r\n\r\nif __name__ ==\
    \ '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\ShortestPath\dijkstra_v2.py
  isVerificationFile: true
  path: TestCase\AOJ\ALDS1_12_B.test.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\ALDS1_12_B.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\ALDS1_12_B.test.py
- /verify\TestCase\AOJ\ALDS1_12_B.test.py.html
title: TestCase\AOJ\ALDS1_12_B.test.py
---
