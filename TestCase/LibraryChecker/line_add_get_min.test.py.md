---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\LiChaoTree.py
    title: Li-Chao Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/line_add_get_min
    links:
    - https://judge.yosupo.jp/problem/line_add_get_min
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.SegmentTree.LiChaoTree\
    \ import LiChaoTree\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    lines = [list(map(int, input().split())) for i in range(n)]\r\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\r\n    INF = 10 ** 20\r\
    \n\r\n    xs = []\r\n    for flag, *query in queries:\r\n        if flag:\r\n\
    \            xs.append(query[0])\r\n\r\n    lct = LiChaoTree(xs)\r\n    for line\
    \ in lines:\r\n        lct.add_line(line)\r\n\r\n    ans = []\r\n    for flag,\
    \ *query in queries:\r\n        if flag == 0:\r\n            line = query\r\n\
    \            lct.add_line(line)\r\n        else:\r\n            p = query[0]\r\
    \n            ans.append(lct.min(p))\r\n\r\n    print(\"\\n\".join(map(str, ans)))\r\
    \n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\SegmentTree\LiChaoTree.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\line_add_get_min.test.py
  requiredBy: []
  timestamp: '2021-01-03 06:18:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\line_add_get_min.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\line_add_get_min.test.py
- /verify\TestCase\LibraryChecker\line_add_get_min.test.py.html
title: TestCase\LibraryChecker\line_add_get_min.test.py
---
