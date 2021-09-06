---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/dsu_on_tree.py
    title: DSU on tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\nfrom Graph.Tree.dsu_on_tree import dsu_on_tree\n\n\
    \ndef main():\n    n, q = map(int, input().split())\n    a = list(map(int, input().split()))\n\
    \    p = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u, v in enumerate(p):\n\
    \        u += 1\n        tree[u].append(v)\n        tree[v].append(u)\n\n    ans\
    \ = [-1] * (q + 1)\n    update = [[] for i in range(n)]\n    answer = [[] for\
    \ i in range(n)]\n    for i in range(n):\n        update[i].append((0, a[i]))\n\
    \    for t, (flag, *qu) in enumerate(queries, 1):\n        if flag == 0:\n   \
    \         u, x = qu\n            update[u].append((t, x))\n        else:\n   \
    \         u = qu[0]\n            answer[u].append(t)\n\n    bit = BinaryIndexedTree(q\
    \ + 1)\n\n    def add(v):\n        for t, val in update[v]:\n            bit.add(t,\
    \ val)\n\n    def sub(v):\n        for t, val in update[v]:\n            bit.add(t,\
    \ -val)\n\n    def query(v):\n        for t in answer[v]:\n            ans[t]\
    \ = bit.sum(0, t)\n\n    dsu_on_tree(tree, 0, add, sub, query)\n    print(\"\\\
    n\".join(map(str, [val for val in ans if val != -1])))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Graph/Tree/dsu_on_tree.py
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
  requiredBy: []
  timestamp: '2021-07-24 16:52:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
- /verify/TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py.html
title: TestCase/LibraryChecker/vertex_add_subtree_sum.dsu_on_tree.test.py
---
