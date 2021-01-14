---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Decomposition/SCC_Kosaraju.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\
      \u30B4\u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\nimport\
    \ sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Decomposition.SCC_Kosaraju\
    \ import StronglyConnectedComponents\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n\n    scc =\
    \ StronglyConnectedComponents(n)\n    for v, nxt_v in edges:\n        scc.add_edge(v,\
    \ nxt_v)\n    scc.build()\n    _, elems = scc.construct_dag()\n\n    print(len(elems))\n\
    \    for res in elems:\n        print(len(res), *res)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/Decomposition/SCC_Kosaraju.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/scc.Kosaraju.test.py
  requiredBy: []
  timestamp: '2021-01-09 01:19:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/scc.Kosaraju.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/scc.Kosaraju.test.py
- /verify/TestCase/LibraryChecker/scc.Kosaraju.test.py.html
title: TestCase/LibraryChecker/scc.Kosaraju.test.py
---
