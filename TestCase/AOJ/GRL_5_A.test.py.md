---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Tree\rerooting.py
    title: "\u5168\u65B9\u4F4D\u6728DP (Re-Rooting)"
  - icon: ':heavy_check_mark:'
    path: Graph\edge_to_vertex.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_A\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.Tree.rerooting\
    \ import rerooting\r\nfrom Graph.edge_to_vertex import edge_to_vertex\r\n\r\n\r\
    \ndef main():\r\n    n = int(input())\r\n    edges = [list(map(int, input().split()))\
    \ for i in range(n - 1)]\r\n    edges, vals = edge_to_vertex(n, edges)\r\n\r\n\
    \    unit = (0, 0)\r\n\r\n    def merge(a, b):\r\n        if a[0] > b[0]:\r\n\
    \            return (a[0], b[0])\r\n        return (b[0], a[0])\r\n\r\n    def\
    \ addnode(a, v):\r\n        return (a[0] + vals[v], a[1] + vals[v])\r\n\r\n  \
    \  ans = rerooting(n + n - 1, edges, unit, merge, addnode)\r\n    print(max([l1\
    \ + l2 for l1, l2 in ans[:n]]))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\
    \n"
  dependsOn:
  - Graph\Tree\rerooting.py
  - Graph\edge_to_vertex.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_5_A.test.py
  requiredBy: []
  timestamp: '2021-01-14 15:36:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_5_A.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_5_A.test.py
- /verify\TestCase\AOJ\GRL_5_A.test.py.html
title: TestCase\AOJ\GRL_5_A.test.py
---
