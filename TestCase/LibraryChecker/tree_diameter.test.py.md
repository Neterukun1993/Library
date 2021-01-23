---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Tree\diameter.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.Tree.diameter\
    \ import diameter\r\n\r\n\r\ndef main():\r\n    n = int(input())\r\n    edges\
    \ = [list(map(int, input().split())) for _ in range(n - 1)]\r\n\r\n    tree =\
    \ [[] for i in range(n)]\r\n    for a, b, cost in edges:\r\n        tree[a].append((b,\
    \ cost))\r\n        tree[b].append((a, cost))\r\n\r\n    diam, path = diameter(tree)\r\
    \n    print(diam, len(path))\r\n    print(*path)\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - Graph\Tree\diameter.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\tree_diameter.test.py
  requiredBy: []
  timestamp: '2021-01-11 01:21:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\tree_diameter.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\tree_diameter.test.py
- /verify\TestCase\LibraryChecker\tree_diameter.test.py.html
title: TestCase\LibraryChecker\tree_diameter.test.py
---
