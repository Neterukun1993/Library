---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from functools import cmp_to_key\n\n\ndef atan2_sorted(points):\n    def\
    \ cmp(p1, p2):\n        x1, y1 = p1\n        x2, y2 = p2\n        if x1 * y2 -\
    \ y1 * x2 < 0: return 1\n        elif x1 * y2 - y1 * x2 > 0: return -1\n     \
    \   else: return 0\n\n    quadrant = [[] for i in range(4)]\n    for x, y in points:\n\
    \        if x == 0 and y == 0: quadrant[2].append((x, y))\n        elif x <= 0\
    \ and y < 0: quadrant[0].append((x, y))\n        elif x > 0 and y <= 0: quadrant[1].append((x,\
    \ y))\n        elif x >= 0 and y > 0: quadrant[2].append((x, y)) \n        else:\
    \ quadrant[3].append((x, y))\n\n    res = []\n    for i in range(4):\n       \
    \ quadrant[i].sort(key=cmp_to_key(cmp))\n        for p in quadrant[i]:\n     \
    \       res.append(p)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/atan2_sorted.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Geometry/atan2_sorted.py
layout: document
title: "\u504F\u89D2\u30BD\u30FC\u30C8"
---
