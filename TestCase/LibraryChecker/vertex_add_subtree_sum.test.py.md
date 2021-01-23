---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph\Tree\HLDecomposition.py
    title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\r\nfrom Graph.Tree.HLDecomposition import HLDecomposition\r\
    \n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\n    a = list(map(int,\
    \ input().split()))\r\n    p = list(map(int, input().split()))\r\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\r\n\r\n    tree = [[]\
    \ for i in range(n)]\r\n    for u, v in enumerate(p):\r\n        u += 1\r\n  \
    \      tree[u].append(v)\r\n        tree[v].append(u)\r\n\r\n    hld = HLDecomposition(tree)\r\
    \n    bit = BinaryIndexedTree(n)\r\n\r\n    for i, val in enumerate(a):\r\n  \
    \      bit.add(hld[i], val)\r\n\r\n    ans = []\r\n    for flag, *query in queries:\r\
    \n        if flag == 0:\r\n            u, val = query\r\n            bit.add(hld[u],\
    \ val)\r\n        else:\r\n            u = query[0]\r\n            l, r = hld.range_subtree(u)\r\
    \n            ans.append(bit.sum(l, r))\r\n\r\n    print(\"\\n\".join(map(str,\
    \ ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\PointAddRangeSum.py
  - Graph\Tree\HLDecomposition.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
  requiredBy: []
  timestamp: '2021-01-16 03:42:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
- /verify\TestCase\LibraryChecker\vertex_add_subtree_sum.test.py.html
title: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
---
