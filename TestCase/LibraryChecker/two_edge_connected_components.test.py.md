---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Decomposition\TwoEdgeConnectedComponents.py
    title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/two_edge_connected_components
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.Decomposition.TwoEdgeConnectedComponents\
    \ import TwoEdgeConnectedComponents\r\n\r\n\r\ndef main():\r\n    n, m = map(int,\
    \ input().split())\r\n    edges = [list(map(int, input().split())) for i in range(m)]\r\
    \n\r\n    tecc = TwoEdgeConnectedComponents(n)\r\n    for u, v in edges:\r\n \
    \       tecc.add_edge(u, v)\r\n\r\n    tecc.build()\r\n    gp = tecc.groups()\r\
    \n\r\n    print(len(gp))\r\n    for res in gp:\r\n        print(len(res), *res)\r\
    \n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\Decomposition\TwoEdgeConnectedComponents.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\two_edge_connected_components.test.py
  requiredBy: []
  timestamp: '2021-01-10 06:54:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\two_edge_connected_components.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\two_edge_connected_components.test.py
- /verify\TestCase\LibraryChecker\two_edge_connected_components.test.py.html
title: TestCase\LibraryChecker\two_edge_connected_components.test.py
---
