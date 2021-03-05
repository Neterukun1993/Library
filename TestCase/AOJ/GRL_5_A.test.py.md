---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/rerooting.py
    title: "\u5168\u65B9\u4F4D\u6728DP (Re-Rooting)"
  - icon: ':heavy_check_mark:'
    path: Graph/misc/edge_to_vertex.py
    title: "\u8FBA\u60C5\u5831\u3092\u9802\u70B9\u60C5\u5831\u3078\u3068\u5909\u63DB"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.rerooting import\
    \ rerooting\nfrom Graph.misc.edge_to_vertex import edge_to_vertex\n\n\ndef main():\n\
    \    n = int(input())\n    edges = [list(map(int, input().split())) for i in range(n\
    \ - 1)]\n    edges, vals = edge_to_vertex(n, edges)\n\n    unit = (0, 0)\n\n \
    \   def merge(a, b):\n        if a[0] > b[0]:\n            return (a[0], b[0])\n\
    \        return (b[0], a[0])\n\n    def addnode(a, v):\n        return (a[0] +\
    \ vals[v], a[1] + vals[v])\n\n    ans = rerooting(n + n - 1, edges, unit, merge,\
    \ addnode)\n    print(max([l1 + l2 for l1, l2 in ans[:n]]))\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/rerooting.py
  - Graph/misc/edge_to_vertex.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_5_A.test.py
  requiredBy: []
  timestamp: '2021-01-24 18:01:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_5_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_5_A.test.py
- /verify/TestCase/AOJ/GRL_5_A.test.py.html
title: TestCase/AOJ/GRL_5_A.test.py
---
