---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/warshall_floyd.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.ShortestPath.warshall_floyd\
    \ import warshall_floyd\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n    INF = 10\
    \ ** 18\n\n    matrix = [[INF] * n for i in range(n)]\n    for v in range(n):\n\
    \        matrix[v][v] = 0\n    for u, v, cost in edges:\n        matrix[u][v]\
    \ = cost\n\n    dist = warshall_floyd(matrix)\n\n    negative = False\n    for\
    \ v in range(n):\n        if dist[v][v] < 0:\n            negative = True\n\n\
    \    if negative:\n        print(\"NEGATIVE CYCLE\")\n    else:\n        for res\
    \ in dist:\n            print(*[num if num < 10 ** 15 else \"INF\" for num in\
    \ res])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/ShortestPath/warshall_floyd.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_1_C.test.py
  requiredBy: []
  timestamp: '2021-01-15 11:26:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_1_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_1_C.test.py
- /verify/TestCase/AOJ/GRL_1_C.test.py.html
title: TestCase/AOJ/GRL_1_C.test.py
---
