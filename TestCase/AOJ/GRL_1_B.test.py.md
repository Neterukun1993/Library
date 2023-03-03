---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/bellman_ford.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.ShortestPath.bellman_ford\
    \ import bellman_ford\n\n\ndef main():\n    n, m, s = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n    INF = 10\
    \ ** 18\n\n    graph = [[] for i in range(n)]\n    for u, v, cost in edges:\n\
    \        graph[u].append((v, cost))\n\n    negative, dist = bellman_ford(s, graph)\n\
    \    if negative:\n        print(\"NEGATIVE CYCLE\")\n    else:\n        for val\
    \ in dist:\n            if val < 10 ** 15:\n                print(val)\n     \
    \       else:\n                print(\"INF\")\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/ShortestPath/bellman_ford.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_1_B.test.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_1_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_1_B.test.py
- /verify/TestCase/AOJ/GRL_1_B.test.py.html
title: TestCase/AOJ/GRL_1_B.test.py
---
