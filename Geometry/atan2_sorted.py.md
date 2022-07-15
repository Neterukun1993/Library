---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/sort_points_by_argument.test.py
    title: TestCase/LibraryChecker/sort_points_by_argument.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def atan2_sorted(points):\n    class Cmp:\n        def __init__(self, obj):\n\
    \            self.obj = obj\n\n        def __lt__(self, other):\n            return\
    \ self.cmp(self.obj, other.obj) < 0\n\n        def cmp(self, p1, p2):\n      \
    \      x1, y1 = p1\n            x2, y2 = p2\n            if x1 * y2 - y1 * x2\
    \ < 0: return 1\n            elif x1 * y2 - y1 * x2 > 0: return -1\n         \
    \   else: return 0\n\n    quadrant = [[] for i in range(4)]\n    for x, y in points:\n\
    \        if x == 0 and y == 0: quadrant[2].append((x, y))\n        elif x <= 0\
    \ and y < 0: quadrant[0].append((x, y))\n        elif x > 0 and y <= 0: quadrant[1].append((x,\
    \ y))\n        elif x >= 0 and y > 0: quadrant[2].append((x, y))\n        else:\
    \ quadrant[3].append((x, y))\n\n    res = []\n    for i in range(4):\n       \
    \ quadrant[i].sort(key=Cmp)\n        for p in quadrant[i]:\n            res.append(p)\n\
    \    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/atan2_sorted.py
  requiredBy: []
  timestamp: '2021-05-07 00:33:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/sort_points_by_argument.test.py
documentation_of: Geometry/atan2_sorted.py
layout: document
title: "\u504F\u89D2\u30BD\u30FC\u30C8"
---

## 概要
点の集合を偏角の大きさ (atan2 の大きさ) によってソートする。

## 使い方
`atan2_sorted(points: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]`  
$N$ 個の点 `points` を偏角ソートした結果を返す。点は ($x$ 座標, $y$ 座標) で与える。計算量 $O(N \log N)$
