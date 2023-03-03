---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/EnumerableUnionFind.py
    title: Enumerable Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.EnumerableUnionFind\
    \ import EnumerableUnionFind\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    euf\
    \ = EnumerableUnionFind(n)\n    ans = []\n    for flag, x, y in queries:\n   \
    \     if flag == 0:\n            euf.merge(x, y)\n        else:\n            ans.append(int(euf.same(x,\
    \ y)))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/UnionFind/EnumerableUnionFind.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
  requiredBy: []
  timestamp: '2022-08-20 05:25:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
- /verify/TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py.html
title: TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
---
