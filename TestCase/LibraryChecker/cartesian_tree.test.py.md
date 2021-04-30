---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/cartesian_tree.py
    title: Cartesian Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cartesian_tree
    links:
    - https://judge.yosupo.jp/problem/cartesian_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Tree.cartesian_tree\
    \ import cartesian_tree\n\n\ndef main():\n    n = int(input())\n    a = list(map(int,\
    \ input().split()))\n\n    par = cartesian_tree(a)\n    print(*[p if p != -1 else\
    \ i for i, p in enumerate(par)])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Tree/cartesian_tree.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/cartesian_tree.test.py
  requiredBy: []
  timestamp: '2021-02-03 22:14:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/cartesian_tree.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/cartesian_tree.test.py
- /verify/TestCase/LibraryChecker/cartesian_tree.test.py.html
title: TestCase/LibraryChecker/cartesian_tree.test.py
---
