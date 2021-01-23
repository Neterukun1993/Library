---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\misc\cycle_detection.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.misc.cycle_detection\
    \ import cycle_detection\r\n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for _ in range(m)]\r\n\r\n    graph\
    \ = [[] for i in range(n)]\r\n    edge_idx = {}\r\n    for i, (u, v) in enumerate(edges):\r\
    \n        graph[u].append(v)\r\n        edge_idx[u, v] = i\r\n\r\n    cycle =\
    \ cycle_detection(graph)\r\n    if not cycle:\r\n        print(-1)\r\n    else:\r\
    \n        print(len(cycle))\r\n        for u, v in zip(cycle[0:], cycle[1:] +\
    \ [cycle[0]]):\r\n            print(edge_idx[u, v])\r\n\r\n\r\nif __name__ ==\
    \ '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\misc\cycle_detection.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\cycle_detection.test.py
  requiredBy: []
  timestamp: '2021-01-14 17:41:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\cycle_detection.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\cycle_detection.test.py
- /verify\TestCase\LibraryChecker\cycle_detection.test.py.html
title: TestCase\LibraryChecker\cycle_detection.test.py
---
