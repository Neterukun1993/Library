---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Tree\EulerTour.py
    title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (LCA)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\r\nimport\
    \ sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.Tree.EulerTour import\
    \ EulerTour\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\n\
    \    p = list(map(int, input().split()))\r\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\r\n\r\n    tree = [[] for i in range(n)]\r\n    for u, v\
    \ in enumerate(p):\r\n        u += 1\r\n        tree[u].append(v)\r\n        tree[v].append(u)\r\
    \n\r\n    et = EulerTour(tree, 0)\r\n    et.build_lca()\r\n    ans = []\r\n  \
    \  for u, v in queries:\r\n        ans.append(et.lca(u, v))\r\n\r\n    print('\\\
    n'.join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\Tree\EulerTour.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\lca.EulerTour.test.py
  requiredBy: []
  timestamp: '2021-01-07 06:39:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\lca.EulerTour.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\lca.EulerTour.test.py
- /verify\TestCase\LibraryChecker\lca.EulerTour.test.py.html
title: TestCase\LibraryChecker\lca.EulerTour.test.py
---
