---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':question:'
    path: Graph/Tree/HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\nfrom Graph.Tree.HLDecomposition import HLDecomposition\n\
    \n\ndef main():\n    n = int(input())\n    nodes = [list(map(int, input().split()))\
    \ for i in range(n)]\n    q = int(input())\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u in range(n):\n\
    \        for v in nodes[u][1:]:\n            tree[u].append(v)\n            tree[v].append(u)\n\
    \n    hld = HLDecomposition(tree)\n    bit = BinaryIndexedTree(n)\n\n    ans =\
    \ []\n    for flag, *query in queries:\n        if flag == 0:\n            v,\
    \ val = query\n            bit.add(hld[v], val)\n        else:\n            v\
    \ = query[0]\n            res = 0\n            for l, r in hld.range_edge_path(0,\
    \ v):\n                res += bit.sum(l, r)\n            ans.append(res)\n\n \
    \   print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  - Graph/Tree/HLDecomposition.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_5_D.test.py
  requiredBy: []
  timestamp: '2021-01-16 04:24:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_5_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_5_D.test.py
- /verify/TestCase/AOJ/GRL_5_D.test.py.html
title: TestCase/AOJ/GRL_5_D.test.py
---
