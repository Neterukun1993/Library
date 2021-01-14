---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/SpanningTree/directed_mst.py
    title: "\u6700\u5C0F\u6709\u5411\u5168\u57DF\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/directedmst
    links:
    - https://judge.yosupo.jp/problem/directedmst
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.SpanningTree.directed_mst\
    \ import directed_mst\n\n\ndef main():\n    n, m, root = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n\n    res, par\
    \ = directed_mst(n, edges, root)\n    if res == -1:\n        print(res)\n    else:\n\
    \        print(res)\n        print(*[p if p != -1 else i for i, p in enumerate(par)])\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/SpanningTree/directed_mst.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/directedmst.test.py
  requiredBy: []
  timestamp: '2021-01-14 12:29:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/directedmst.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/directedmst.test.py
- /verify/TestCase/LibraryChecker/directedmst.test.py.html
title: TestCase/LibraryChecker/directedmst.test.py
---
