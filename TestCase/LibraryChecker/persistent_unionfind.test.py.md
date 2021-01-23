---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\PersistentUnionFind.py
    title: "\u6C38\u7D9AUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/persistent_unionfind
    links:
    - https://judge.yosupo.jp/problem/persistent_unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.UnionFind.PersistentUnionFind\
    \ import PersistentUnionFind\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    queries = [list(map(int, input().split())) for i in range(q)]\r\n\r\n  \
    \  uf = PersistentUnionFind(n)\r\n    states = [None] * (q + 1)\r\n    states[-1]\
    \ = uf.rt\r\n\r\n    ans = []\r\n    for i, (flag, k, u, v) in enumerate(queries):\r\
    \n        if flag == 0:\r\n            states[i] = uf.merge(u, v, states[k])\r\
    \n        else:\r\n            if uf.same(u, v, states[k]):\r\n              \
    \  ans.append(1)\r\n            else:\r\n                ans.append(0)\r\n\r\n\
    \    print(\"\\n\".join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - DataStructure\UnionFind\PersistentUnionFind.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\persistent_unionfind.test.py
  requiredBy: []
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\persistent_unionfind.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\persistent_unionfind.test.py
- /verify\TestCase\LibraryChecker\persistent_unionfind.test.py.html
title: TestCase\LibraryChecker\persistent_unionfind.test.py
---
