---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.UnionFind\
    \ import UnionFind\n\n\ndef main():\n    n, q = map(int, input().split())\n  \
    \  queries = [list(map(int, input().split())) for i in range(q)]\n\n    uf = UnionFind(n)\n\
    \    ans = []\n    for flag, x, y in queries:\n        if flag == 0:\n       \
    \     uf.merge(x, y)\n        else:\n            ans.append(int(uf.same(x, y)))\n\
    \n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_1_A.test.py
  requiredBy: []
  timestamp: '2021-01-02 02:09:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_1_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_1_A.test.py
- /verify/TestCase/AOJ/DSL_1_A.test.py.html
title: TestCase/AOJ/DSL_1_A.test.py
---
