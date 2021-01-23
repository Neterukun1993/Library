---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/UnionFind/UnionFindWithPotential.py
    title: "\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u4ED8\u304DUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.UnionFindWithPotential\
    \ import UnionFindWithPotential\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    INF\
    \ = 10 ** 18\n    ufp = UnionFindWithPotential(n)\n    ans = []\n    for flag,\
    \ *query in queries:\n        if flag == 0:\n            x, y, p = query\n   \
    \         ufp.merge(x, y, p)\n        else:\n            x, y = query\n      \
    \      p = ufp.diff(x, y)\n            ans.append(str(p) if p != INF else \"?\"\
    )\n\n    print('\\n'.join(ans))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFindWithPotential.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_1_B.test.py
  requiredBy: []
  timestamp: '2021-01-02 02:55:57+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_1_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_1_B.test.py
- /verify/TestCase/AOJ/DSL_1_B.test.py.html
title: TestCase/AOJ/DSL_1_B.test.py
---
