---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.RangeAddRangeSum\
    \ import BinaryIndexedTree\nfrom Graph.Tree.HLDecomposition import HLDecomposition\n\
    \n\ndef main():\n    n = int(input())\n    nodes = [list(map(int, input().split()))\
    \ for i in range(n)]\n    q = int(input())\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u in range(n):\n\
    \        for v in nodes[u][1:]:\n            tree[u].append(v)\n            tree[v].append(u)\n\
    \n    hld = HLDecomposition(tree)\n    bit = BinaryIndexedTree(n)\n\n    ans =\
    \ []\n    for flag, *query in queries:\n        if flag == 0:\n            v,\
    \ val = query\n            for l, r in hld.range_edge_path(0, v):\n          \
    \      bit.add(l, r, val)\n        else:\n            v = query[0]\n         \
    \   res = 0\n            for l, r in hld.range_edge_path(0, v):\n            \
    \    res += bit.sum(l, r)\n            ans.append(res)\n\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/HLDecomposition.py
  - DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_5_E.test.py
  requiredBy: []
  timestamp: '2021-07-18 03:57:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_5_E.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_5_E.test.py
- /verify/TestCase/AOJ/GRL_5_E.test.py.html
title: TestCase/AOJ/GRL_5_E.test.py
---
