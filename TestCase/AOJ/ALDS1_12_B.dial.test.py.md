---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/dial.py
    title: "Dial\u2019s Algorithm"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.ShortestPath.dial import\
    \ dial\n\n\ndef main():\n    n = int(input())\n    info = [list(map(int, input().split()))\
    \ for i in range(n)]\n    INF = 10 ** 18\n\n    graph = [[] * n for i in range(n)]\n\
    \    max_cost = 0\n    for v in range(n):\n        for j in range(1, len(info[v])\
    \ // 2):\n            nxt_v, cost = info[v][slice(2 * j, 2 * (j + 1))]\n     \
    \       graph[v].append((nxt_v, cost))\n            max_cost = max(max_cost, cost)\n\
    \n    dist = dial(graph, 0, max_cost)\n    for v, ans in enumerate(dist):\n  \
    \      print(v, ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/ShortestPath/dial.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_12_B.dial.test.py
  requiredBy: []
  timestamp: '2021-06-02 23:10:54+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_12_B.dial.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_12_B.dial.test.py
- /verify/TestCase/AOJ/ALDS1_12_B.dial.test.py.html
title: TestCase/AOJ/ALDS1_12_B.dial.test.py
---
