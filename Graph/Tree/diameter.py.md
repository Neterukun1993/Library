---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/tree_diameter.test.py
    title: TestCase/LibraryChecker/tree_diameter.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def diameter(tree):\n    def _dfs(start):\n        dist = [-1] * n\n    \
    \    dist[start] = 0\n        stack = [start]\n        while stack:\n        \
    \    v = stack.pop()\n            for nxt_v, cost in tree[v]:\n              \
    \  if dist[nxt_v] != -1:\n                    continue\n                dist[nxt_v]\
    \ = dist[v] + cost\n                stack.append(nxt_v)\n        max_d = max(dist)\n\
    \        return dist.index(max_d), max_d, dist\n\n    n = len(tree)\n    u, _,\
    \ _ = _dfs(0)\n    v, diam, dist = _dfs(u)\n    path = [v]\n    while v != u:\n\
    \        for nxt_v, cost in tree[v]:\n            if cost + dist[nxt_v] == dist[v]:\n\
    \                path.append(nxt_v)\n                v = nxt_v\n             \
    \   break\n    return diam, path\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/diameter.py
  requiredBy: []
  timestamp: '2021-01-11 01:21:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/tree_diameter.test.py
documentation_of: Graph/Tree/diameter.py
layout: document
title: "\u6728\u306E\u76F4\u5F84"
---

## 概要
木の直径を求めるアルゴリズム。

## 使い方
`diameter(tree: Sequence[Iterable[Tuple[int, int]]]) -> Tuple[int, List[int]]`  
隣接リストで表現された重み付き木 `tree` の直径とそのパスを返す。計算量 $O(V)$
