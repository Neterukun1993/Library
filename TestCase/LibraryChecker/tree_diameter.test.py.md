---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/diameter.py
    title: "\u6728\u306E\u76F4\u5F84"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tree_diameter
    links:
    - https://judge.yosupo.jp/problem/tree_diameter
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.diameter import\
    \ diameter\n\n\ndef main():\n    n = int(input())\n    edges = [list(map(int,\
    \ input().split())) for _ in range(n - 1)]\n\n    tree = [[] for i in range(n)]\n\
    \    for a, b, cost in edges:\n        tree[a].append((b, cost))\n        tree[b].append((a,\
    \ cost))\n\n    diam, path = diameter(tree)\n    print(diam, len(path))\n    print(*path)\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/diameter.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/tree_diameter.test.py
  requiredBy: []
  timestamp: '2021-01-11 01:21:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/tree_diameter.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/tree_diameter.test.py
- /verify/TestCase/LibraryChecker/tree_diameter.test.py.html
title: TestCase/LibraryChecker/tree_diameter.test.py
---
