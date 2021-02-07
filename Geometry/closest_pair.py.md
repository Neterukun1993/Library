---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/CGL_5_A.test.py
    title: TestCase/AOJ/CGL_5_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def merge(ps_l, ps_r):\n    \"\"\"merge the two lists sorted by y-coordinates\
    \ into one.\"\"\"\n    szl, szr = len(ps_l), len(ps_r)\n    ps = []\n    il, ir\
    \ = 0, 0\n    for i in range(szl + szr):\n        if ir == szr:\n            ps.append(ps_l[il])\n\
    \            il += 1\n        elif il == szl:\n            ps.append(ps_r[ir])\n\
    \            ir += 1\n        elif ps_l[il][1] < ps_r[ir][1]:\n            ps.append(ps_l[il])\n\
    \            il += 1\n        else:\n            ps.append(ps_r[ir])\n       \
    \     ir += 1\n    return ps\n\n\ndef closest_pair(points):\n    \"\"\"calculate\
    \ closest pair's distance by divide-and-conquer.\"\"\"\n    INF = 1.0 * 10 **\
    \ 9\n    size = len(points)\n    if size <= 1:\n        return INF, points\n \
    \   mid = size // 2\n    x_mid = points[mid][0]\n    dist_l, ps_l = closest_pair(points[0:mid])\n\
    \    dist_r, ps_r = closest_pair(points[mid:size])\n    dist = min(dist_l, dist_r)\n\
    \    ps = merge(ps_l, ps_r)\n\n    qs = []\n    for xp, yp in ps:\n        if\
    \ abs(xp - x_mid) >= dist:\n            continue\n        for xq, yq in reversed(qs):\n\
    \            dx = xp - xq\n            dy = yp - yq\n            if dy >= dist:\n\
    \                break\n            dist = min((dx ** 2 + dy ** 2) ** 0.5, dist)\n\
    \        qs.append((xp, yp))\n    return dist, ps\n"
  dependsOn: []
  isVerificationFile: false
  path: Geometry/closest_pair.py
  requiredBy: []
  timestamp: '2021-02-07 11:37:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/CGL_5_A.test.py
documentation_of: Geometry/closest_pair.py
layout: document
redirect_from:
- /library/Geometry/closest_pair.py
- /library/Geometry/closest_pair.py.html
title: Geometry/closest_pair.py
---
