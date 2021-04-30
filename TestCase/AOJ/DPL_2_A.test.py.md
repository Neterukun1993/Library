---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/ShortestPath/tsp.py
    title: "\u5DE1\u56DE\u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\u984C"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.ShortestPath.tsp import\
    \ tsp\n\n\ndef main():\n    n, m = map(int, input().split())\n    edges = [list(map(int,\
    \ input().split())) for i in range(m)]\n    INF = 10 ** 18\n\n    matrix = [[INF]\
    \ * n for i in range(n)]\n    for a, b, cost in edges:\n        matrix[a][b] =\
    \ cost\n    for i in range(n):\n        matrix[i][i] = 0\n\n    ans, path = tsp(matrix)\n\
    \    if ans == INF:\n        print(-1)\n    else:\n        print(ans)\n\n\nif\
    \ __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/ShortestPath/tsp.py
  isVerificationFile: true
  path: TestCase/AOJ/DPL_2_A.test.py
  requiredBy: []
  timestamp: '2021-01-24 02:57:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DPL_2_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DPL_2_A.test.py
- /verify/TestCase/AOJ/DPL_2_A.test.py.html
title: TestCase/AOJ/DPL_2_A.test.py
---
