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
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.rerooting import\
    \ rerooting\nfrom Graph.misc.edge_to_vertex import edge_to_vertex\n\n\ndef main():\n\
    \    n = int(input())\n    edges = [list(map(int, input().split())) for i in range(n\
    \ - 1)]\n\n    edges, vals = edge_to_vertex(n, edges)\n    ans = rerooting(n +\
    \ n - 1, edges, 0, max, lambda val, v: val + vals[v])\n\n    print('\\n'.join(map(str,\
    \ ans[:n])))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/edge_to_vertex.py
  - Graph/Tree/rerooting.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_5_B.test.py
  requiredBy: []
  timestamp: '2021-01-24 18:01:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_5_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_5_B.test.py
- /verify/TestCase/AOJ/GRL_5_B.test.py.html
title: TestCase/AOJ/GRL_5_B.test.py
---
