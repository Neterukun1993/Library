---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/CGL_4_A.test.py
    title: TestCase/AOJ/CGL_4_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def convexhull(points):\n    def ccw(p0, p1, p2):\n        v1 = p1[0] - p0[0],\
    \ p1[1] - p0[1]\n        v2 = p2[0] - p0[0], p2[1] - p0[1]\n        crs = v1[0]\
    \ * v2[1] - v1[1] * v2[0]\n        if crs > 0: return 1  # \u53CD\u6642\u8A08\u56DE\
    \u308A\n        if crs < 0: return -1  # \u6642\u8A08\u56DE\u308A\n        return\
    \ 0  # \u76F4\u7DDA\u4E0A\n\n    ps = sorted(points)\n    if len(ps) <= 2:\n \
    \       return ps\n\n    lower = [ps[0], ps[1]]\n    upper = [ps[0], ps[1]]\n\
    \    for p in ps[2:]:\n        while len(lower) >= 2 and ccw(lower[-2], lower[-1],\
    \ p) < 0:\n            lower.pop()\n        lower.append(p)\n        while len(upper)\
    \ >= 2 and ccw(upper[-2], upper[-1], p) > 0:\n            upper.pop()\n      \
    \  upper.append(p)\n    return lower + upper[::-1][1:-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/convexhull.py
  requiredBy: []
  timestamp: '2021-05-16 16:23:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/CGL_4_A.test.py
documentation_of: Geometry/convexhull.py
layout: document
title: "\u51F8\u5305"
---

## 概要
点集合に対する凸包を求めるアルゴリズム。

## 使い方
`convexhull(points: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]`  
2次元平面上の $N$ 個の点集合 `points` に対する凸包を返す。凸包の頂点で最も左にあるものの中で、最も下にある頂点から順に、反時計回りで返す。計算量 $O(N\log N)$
