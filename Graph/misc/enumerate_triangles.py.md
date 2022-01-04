---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/enumerate_triangles.test.py
    title: TestCase/LibraryChecker/enumerate_triangles.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def enumerate_triangles(edges, v_vals, MOD):\n    n = len(v_vals)\n    degs\
    \ = [0] * n\n    for u, v in edges:\n        degs[u] += 1\n        degs[v] +=\
    \ 1\n\n    graph = [[] for i in range(n)]\n    for u, v in edges:\n        if\
    \ v > u:\n            u, v = v, u\n        if degs[u] > degs[v]:\n           \
    \ u, v = v, u\n        graph[u].append(v)\n\n    cnt = 0\n    res = 0\n    flags\
    \ = [False] * n\n\n    # v -> nxt_v1, v -> nxt_v2 -> nxtnxt_v \u306B\u3064\u3044\
    \u3066 nxt_v1 = nxtnxt_v \n    # \u6E80\u305F\u3059\u9802\u70B9\u7D44\u3092\u6570\
    \u3048\u4E0A\u3052\u308B\n    for v in range(n):\n        for nxt_v in graph[v]:\n\
    \            flags[nxt_v] = True\n        for nxt_v in graph[v]:\n           \
    \ for nxtnxt_v in graph[nxt_v]:\n                if flags[nxtnxt_v]:\n       \
    \             cnt += 1\n                    res += v_vals[v] * v_vals[nxt_v] *\
    \ v_vals[nxtnxt_v]\n                    res %= MOD\n        for nxt_v in graph[v]:\n\
    \            flags[nxt_v] = False\n\n    return cnt, res\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/enumerate_triangles.py
  requiredBy: []
  timestamp: '2021-01-21 18:47:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/enumerate_triangles.test.py
documentation_of: Graph/misc/enumerate_triangles.py
layout: document
title: "\u4E09\u89D2\u5F62\u306E\u6570\u3048\u4E0A\u3052"
---
