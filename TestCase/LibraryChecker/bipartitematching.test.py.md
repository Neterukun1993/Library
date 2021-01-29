---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Flow.BipartiteGraph import\
    \ BipartiteGraph\n\n\ndef main():\n    l, r, m = map(int, input().split())\n \
    \   edges = [list(map(int, input().split())) for i in range(m)]\n\n    bg = BipartiteGraph(l,\
    \ r)\n    for vl, vr in edges:\n        bg.add_edge(vl, vr)\n\n    ans = bg.maximum_matching()\n\
    \    edges = bg.matching_edges()\n\n    print(ans)\n    for res in edges:\n  \
    \      print(*res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: TestCase/LibraryChecker/bipartitematching.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/bipartitematching.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/bipartitematching.test.py
- /verify/TestCase/LibraryChecker/bipartitematching.test.py.html
title: TestCase/LibraryChecker/bipartitematching.test.py
---
