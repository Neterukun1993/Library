---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Flow/BipartiteMatching.py
    title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u306E\u30DE\u30C3\u30C1\u30F3\u30B0"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Flow.BipartiteMatching import\
    \ BipartiteMatching\n\n\ndef main():\n    l, r, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n\n    bm = BipartiteMatching(l,\
    \ r)\n    for vl, vr in edges:\n        bm.add_edge(vl, vr)\n\n    ans = bm.maximum_matching()\n\
    \    edges = bm.matching_edges()\n\n    print(ans)\n    for res in edges:\n  \
    \      print(*res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Flow/BipartiteMatching.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/bipartitematching.test.py
  requiredBy: []
  timestamp: '2022-01-15 20:42:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/bipartitematching.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/bipartitematching.test.py
- /verify/TestCase/LibraryChecker/bipartitematching.test.py.html
title: TestCase/LibraryChecker/bipartitematching.test.py
---
