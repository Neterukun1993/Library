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
    PROBLEM: https://judge.yosupo.jp/problem/segment_add_get_min
    links:
    - https://judge.yosupo.jp/problem/segment_add_get_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.LiChaoTree\
    \ import LiChaoTree\n\n\ndef main():\n    n, q = map(int, input().split())\n \
    \   segs = [list(map(int, input().split())) for i in range(n)]\n    queries =\
    \ [list(map(int, input().split())) for i in range(q)]\n    INF = 10 ** 18\n\n\
    \    xs = []\n    for flag, *query in queries:\n        if flag:\n           \
    \ xs.append(query[0])\n\n    lct = LiChaoTree(xs)\n    for l, r, a, b in segs:\n\
    \        line = (a, b)\n        lct.add_seg(line, l, r)\n\n    ans = []\n    for\
    \ flag, *query in queries:\n        if flag == 0:\n            l, r, a, b = query\n\
    \            line = (a, b)\n            lct.add_seg(line, l, r)\n        else:\n\
    \            p = query[0]\n            res = lct.min(p)\n            if res ==\
    \ INF:\n                ans.append(\"INFINITY\")\n            else:\n        \
    \        ans.append(str(res))\n\n    print(\"\\n\".join(map(str, ans)))\n\n\n\
    if __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/LiChaoTree.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/segment_add_get_min.test.py
  requiredBy: []
  timestamp: '2021-01-03 06:25:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/segment_add_get_min.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/segment_add_get_min.test.py
- /verify/TestCase/LibraryChecker/segment_add_get_min.test.py.html
title: TestCase/LibraryChecker/segment_add_get_min.test.py
---
