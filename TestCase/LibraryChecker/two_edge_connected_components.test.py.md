---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Decomposition/TwoEdgeConnectedComponents.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Decomposition.TwoEdgeConnectedComponents\
    \ import TwoEdgeConnectedComponents\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n\n    tecc =\
    \ TwoEdgeConnectedComponents(n)\n    for u, v in edges:\n        tecc.add_edge(u,\
    \ v)\n\n    tecc.build()\n    gp = tecc.groups()\n\n    print(len(gp))\n    for\
    \ res in gp:\n        print(len(res), *res)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/Decomposition/TwoEdgeConnectedComponents.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/two_edge_connected_components.test.py
  requiredBy: []
  timestamp: '2021-01-28 21:03:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/two_edge_connected_components.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/two_edge_connected_components.test.py
- /verify/TestCase/LibraryChecker/two_edge_connected_components.test.py.html
title: TestCase/LibraryChecker/two_edge_connected_components.test.py
---
