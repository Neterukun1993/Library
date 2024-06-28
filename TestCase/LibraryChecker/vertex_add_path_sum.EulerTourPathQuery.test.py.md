---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/EulerTourPathQuery.py
    title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (\u30D1\u30B9\u306B\u5BFE\u3059\
      \u308B\u30AF\u30A8\u30EA)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.EulerTourPathQuery\
    \ import EulerTourPathQuery\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    edges = [list(map(int, input().split()))\
    \ for i in range(n - 1)]\n    queries = [list(map(int, input().split())) for i\
    \ in range(q)]\n\n    tree = [[] for i in range(n)]\n    for u, v in edges:\n\
    \        tree[u].append(v)\n        tree[v].append(u)\n\n    et = EulerTourPathQuery(tree)\n\
    \    et.build(a)\n\n    ans = []\n    for flag, u, v in queries:\n        if flag\
    \ == 0:\n            val = v\n            et.add(u, val)\n        else:\n    \
    \        ans.append(et.vertex_path_sum(u, v))\n\n    print(\"\\n\".join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/EulerTourPathQuery.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
  requiredBy: []
  timestamp: '2021-06-15 21:41:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
- /verify/TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py.html
title: TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
---
