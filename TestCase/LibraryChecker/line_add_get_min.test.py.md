---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/LiChaoTree.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.LiChaoTree\
    \ import LiChaoTree\n\n\ndef main():\n    n, q = map(int, input().split())\n \
    \   lines = [list(map(int, input().split())) for i in range(n)]\n    queries =\
    \ [list(map(int, input().split())) for i in range(q)]\n    INF = 10 ** 20\n\n\
    \    xs = []\n    for flag, *query in queries:\n        if flag:\n           \
    \ xs.append(query[0])\n\n    lct = LiChaoTree(xs)\n    for line in lines:\n  \
    \      lct.add_line(line)\n\n    ans = []\n    for flag, *query in queries:\n\
    \        if flag == 0:\n            line = query\n            lct.add_line(line)\n\
    \        else:\n            p = query[0]\n            ans.append(lct.min(p))\n\
    \n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n   \
    \ main()\n"
  dependsOn:
  - DataStructure/SegmentTree/LiChaoTree.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/line_add_get_min.test.py
  requiredBy: []
  timestamp: '2021-01-03 06:18:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/line_add_get_min.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/line_add_get_min.test.py
- /verify/TestCase/LibraryChecker/line_add_get_min.test.py.html
title: TestCase/LibraryChecker/line_add_get_min.test.py
---
