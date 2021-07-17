---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/KDTree2D.py
    title: "\u4E8C\u6B21\u5143\u9818\u57DF\u63A2\u7D22 (kD-Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.KDTree2D\
    \ import KDTree2D\n\n\ndef main():\n    n = int(input())\n    points = [tuple(map(int,\
    \ input().split())) for i in range(n)]\n    q = int(input())\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n\n    idxs = {}\n    for idx, (x, y) in\
    \ enumerate(points):\n        if (x, y) not in idxs:\n            idxs[x, y] =\
    \ []\n        idxs[x, y].append(idx)\n\n    kd = KDTree2D(set(points))\n    for\
    \ xl, xr, yl, yr in queries:\n        xr += 1\n        yr += 1\n        res =\
    \ []\n        for x, y in kd.find(xl, xr, yl, yr):\n            for idx in idxs[x,\
    \ y]:\n                res.append(idx)\n        res.sort()\n        if res:\n\
    \            print('\\n'.join(map(str, res)))\n            print()\n        else:\n\
    \            print()\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/KDTree2D.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_C.test.py
  requiredBy: []
  timestamp: '2021-02-07 18:49:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_C.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_C.test.py
- /verify/TestCase/AOJ/DSL_2_C.test.py.html
title: TestCase/AOJ/DSL_2_C.test.py
---
