---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/PersistentUnionFind.py
    title: "\u6C38\u7D9AUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_unionfind
    links:
    - https://judge.yosupo.jp/problem/persistent_unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.PersistentUnionFind\
    \ import PersistentUnionFind\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    uf =\
    \ PersistentUnionFind(n)\n    states = [None] * (q + 1)\n    states[-1] = uf.rt\n\
    \n    ans = []\n    for i, (flag, k, u, v) in enumerate(queries):\n        if\
    \ flag == 0:\n            states[i] = uf.merge(u, v, states[k])\n        else:\n\
    \            if uf.same(u, v, states[k]):\n                ans.append(1)\n   \
    \         else:\n                ans.append(0)\n\n    print(\"\\n\".join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/UnionFind/PersistentUnionFind.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/persistent_unionfind.test.py
  requiredBy: []
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/persistent_unionfind.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/persistent_unionfind.test.py
- /verify/TestCase/LibraryChecker/persistent_unionfind.test.py.html
title: TestCase/LibraryChecker/persistent_unionfind.test.py
---
