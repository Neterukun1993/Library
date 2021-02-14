---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/topological_sorted.py
    title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8 (Kahn \u306E\u30A2\
      \u30EB\u30B4\u30EA\u30BA\u30E0)"
  - icon: ':heavy_check_mark:'
    path: Graph/misc/topological_sorted_dfs.py
    title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8 (\u6DF1\u3055\u512A\
      \u5148\u63A2\u7D22)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.topological_sorted\
    \ import topological_sorted as kahn\nfrom Graph.misc.topological_sorted_dfs import\
    \ topological_sorted\n\n\ndef check(graph, tp_order):\n    n = len(graph)\n  \
    \  idxs = [0] * n\n    for i, v in enumerate(tp_order):\n        idxs[v] = i\n\
    \    for v in range(n):\n        for nxt_v in graph[v]:\n            if idxs[v]\
    \ > idxs[nxt_v]:\n                return False\n    return True\n\n\ndef main():\n\
    \    n, m = map(int, input().split())\n    edges = [list(map(int, input().split()))\
    \ for i in range(m)]\n\n    graph = [[] for i in range(n)]\n    for u, v in edges:\n\
    \        graph[u].append(v)\n\n    _, tp_order = kahn(graph)\n    assert(check(graph,\
    \ tp_order))\n\n    tp_order = topological_sorted(graph)\n    assert(check(graph,\
    \ tp_order))\n\n    print('\\n'.join(map(str, tp_order)))\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/topological_sorted_dfs.py
  - Graph/misc/topological_sorted.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_4_B.test.py
  requiredBy: []
  timestamp: '2021-02-15 02:48:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_4_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_4_B.test.py
- /verify/TestCase/AOJ/GRL_4_B.test.py.html
title: TestCase/AOJ/GRL_4_B.test.py
---
