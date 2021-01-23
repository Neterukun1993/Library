---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\ShortestPath\warshall_floyd.py
    title: "\u30EF\u30FC\u30B7\u30E3\u30EB\u30D5\u30ED\u30A4\u30C9\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.ShortestPath.warshall_floyd\
    \ import warshall_floyd\r\n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for i in range(m)]\r\n    INF =\
    \ 10 ** 18\r\n\r\n    matrix = [[INF] * n for i in range(n)]\r\n    for v in range(n):\r\
    \n        matrix[v][v] = 0\r\n    for u, v, cost in edges:\r\n        matrix[u][v]\
    \ = cost\r\n\r\n    dist = warshall_floyd(matrix)\r\n\r\n    negative = False\r\
    \n    for v in range(n):\r\n        if dist[v][v] < 0:\r\n            negative\
    \ = True\r\n\r\n    if negative:\r\n        print(\"NEGATIVE CYCLE\")\r\n    else:\r\
    \n        for res in dist:\r\n            print(*[num if num < 10 ** 15 else \"\
    INF\" for num in res])\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\ShortestPath\warshall_floyd.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_1_C.test.py
  requiredBy: []
  timestamp: '2021-01-15 11:26:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_1_C.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_1_C.test.py
- /verify\TestCase\AOJ\GRL_1_C.test.py.html
title: TestCase\AOJ\GRL_1_C.test.py
---
