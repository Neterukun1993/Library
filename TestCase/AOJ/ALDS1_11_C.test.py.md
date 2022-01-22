---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/bfs.py
    title: BFS
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.ShortestPath.bfs import\
    \ bfs\n\n\ndef main():\n    n = int(input())\n    info = [list(map(int, input().split()))\
    \ for i in range(n)]\n\n    graph = [[] for _ in range(n)]\n    for v, k, *nxt_vs\
    \ in info:\n        v -= 1\n        for nxt_v in nxt_vs:\n            nxt_v -=\
    \ 1\n            graph[v].append(nxt_v)\n\n    dist = bfs(graph, 0)\n    for i,\
    \ d in enumerate(dist):\n        if d == 10 ** 18:\n            print(i + 1, -1)\n\
    \        else:\n            print(i + 1, d)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/ShortestPath/bfs.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_11_C.test.py
  requiredBy: []
  timestamp: '2022-01-22 18:47:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_11_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_11_C.test.py
- /verify/TestCase/AOJ/ALDS1_11_C.test.py.html
title: TestCase/AOJ/ALDS1_11_C.test.py
---
