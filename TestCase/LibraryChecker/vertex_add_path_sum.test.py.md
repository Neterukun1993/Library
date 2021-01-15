---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  - icon: ':question:'
    path: Graph/Tree/HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\nfrom Graph.Tree.HLDecomposition import HLDecomposition\n\
    \n\ndef main():\n    n, q = map(int, input().split())\n    a = list(map(int, input().split()))\n\
    \    edges = [list(map(int, input().split())) for i in range(n - 1)]\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    tree = [[] for\
    \ i in range(n)]\n    for u, v in edges:\n        tree[u].append(v)\n        tree[v].append(u)\n\
    \n    hld = HLDecomposition(tree)\n    bit = BinaryIndexedTree(n)\n\n    for i,\
    \ val in enumerate(a):\n        bit.add(hld[i], val)\n\n    ans = []\n    for\
    \ flag, u, v in queries:\n        if flag == 0:\n            val = v\n       \
    \     bit.add(hld[u], val)\n        else:\n            res = 0\n            for\
    \ l, r in hld.range_vertex_path(u, v):\n                res += bit.sum(l, r)\n\
    \        ans.append(res)\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/HLDecomposition.py
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/vertex_add_path_sum.test.py
  requiredBy: []
  timestamp: '2021-01-16 03:42:28+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/vertex_add_path_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/vertex_add_path_sum.test.py
- /verify/TestCase/LibraryChecker/vertex_add_path_sum.test.py.html
title: TestCase/LibraryChecker/vertex_add_path_sum.test.py
---
