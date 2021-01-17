---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\nfrom Graph.Tree.HLDecomposition import HLDecomposition\n\
    \n\ndef main():\n    n, q = map(int, input().split())\n    a = list(map(int, input().split()))\n\
    \    p = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u, v in enumerate(p):\n\
    \        u += 1\n        tree[u].append(v)\n        tree[v].append(u)\n\n    hld\
    \ = HLDecomposition(tree)\n    bit = BinaryIndexedTree(n)\n\n    for i, val in\
    \ enumerate(a):\n        bit.add(hld[i], val)\n\n    ans = []\n    for flag, *query\
    \ in queries:\n        if flag == 0:\n            u, val = query\n           \
    \ bit.add(hld[u], val)\n        else:\n            u = query[0]\n            l,\
    \ r = hld.range_subtree(u)\n            ans.append(bit.sum(l, r))\n\n    print(\"\
    \\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/HLDecomposition.py
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2021-01-16 03:42:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
- /verify/TestCase/LibraryChecker/vertex_add_subtree_sum.test.py.html
title: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
---
