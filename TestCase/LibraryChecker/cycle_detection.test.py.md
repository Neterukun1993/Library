---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/cycle_detection.py
    title: "\u30B5\u30A4\u30AF\u30EB\u691C\u51FA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection
    links:
    - https://judge.yosupo.jp/problem/cycle_detection
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.cycle_detection\
    \ import cycle_detection\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for _ in range(m)]\n\n    graph\
    \ = [[] for i in range(n)]\n    edge_idx = {}\n    for i, (u, v) in enumerate(edges):\n\
    \        graph[u].append(v)\n        edge_idx[u, v] = i\n\n    cycle = cycle_detection(graph)\n\
    \    if not cycle:\n        print(-1)\n    else:\n        print(len(cycle))\n\
    \        for u, v in zip(cycle[0:], cycle[1:] + [cycle[0]]):\n            print(edge_idx[u,\
    \ v])\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/cycle_detection.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/cycle_detection.test.py
  requiredBy: []
  timestamp: '2021-01-14 17:41:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/cycle_detection.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/cycle_detection.test.py
- /verify/TestCase/LibraryChecker/cycle_detection.test.py.html
title: TestCase/LibraryChecker/cycle_detection.test.py
---
