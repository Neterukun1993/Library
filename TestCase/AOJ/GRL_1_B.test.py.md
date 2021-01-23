---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\ShortestPath\bellman_ford.py
    title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.ShortestPath.bellman_ford\
    \ import bellman_ford\r\n\r\n\r\ndef main():\r\n    n, m, s = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for i in range(m)]\r\n    INF =\
    \ 10 ** 18\r\n\r\n    graph = [[] for i in range(n)]\r\n    for u, v, cost in\
    \ edges:\r\n        graph[u].append((v, cost))\r\n\r\n    negative, dist = bellman_ford(s,\
    \ graph)\r\n    if negative:\r\n        print(\"NEGATIVE CYCLE\")\r\n    else:\r\
    \n        for val in dist:\r\n            if val < 10 ** 15:\r\n             \
    \   print(val)\r\n            else:\r\n                print(\"INF\")\r\n\r\n\r\
    \nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\ShortestPath\bellman_ford.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_1_B.test.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_1_B.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_1_B.test.py
- /verify\TestCase\AOJ\GRL_1_B.test.py.html
title: TestCase\AOJ\GRL_1_B.test.py
---
