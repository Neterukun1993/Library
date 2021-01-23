---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\RangeAddRangeSum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph\Tree\HLDecomposition.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.RangeAddRangeSum\
    \ import BinaryIndexedTree\r\nfrom Graph.Tree.HLDecomposition import HLDecomposition\r\
    \n\r\n\r\ndef main():\r\n    n = int(input())\r\n    nodes = [list(map(int, input().split()))\
    \ for i in range(n)]\r\n    q = int(input())\r\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\r\n\r\n    tree = [[] for i in range(n)]\r\n    for u in\
    \ range(n):\r\n        for v in nodes[u][1:]:\r\n            tree[u].append(v)\r\
    \n            tree[v].append(u)\r\n\r\n    hld = HLDecomposition(tree)\r\n   \
    \ bit = BinaryIndexedTree(n)\r\n\r\n    ans = []\r\n    for flag, *query in queries:\r\
    \n        if flag == 0:\r\n            v, val = query\r\n            for l, r\
    \ in hld.range_edge_path(0, v):\r\n                bit.add(l, r, val)\r\n    \
    \    else:\r\n            v = query[0]\r\n            res = 0\r\n            for\
    \ l, r in hld.range_edge_path(0, v):\r\n                res += bit.sum(l, r)\r\
    \n            ans.append(res)\r\n\r\n    print('\\n'.join(map(str, ans)))\r\n\r\
    \n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\Tree\HLDecomposition.py
  - DataStructure\BinaryIndexedTree\RangeAddRangeSum.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_5_E.test.py
  requiredBy: []
  timestamp: '2021-01-16 04:24:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_5_E.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_5_E.test.py
- /verify\TestCase\AOJ\GRL_5_E.test.py.html
title: TestCase\AOJ\GRL_5_E.test.py
---
