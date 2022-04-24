---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/centroid.py
    title: "\u6728\u306E\u91CD\u5FC3"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/topological_sorted.py
    title: "\u6728\u4E0A\u306E\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2821.test.py
    title: TestCase/AOJ/2821.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph.Tree.centroid import centroid\nfrom Graph.Tree.topological_sorted\
    \ import topological_sorted\n\n\nMAX = 0\nHASHMAP = {}\n\n\ndef treehash(tree,\
    \ root=None):\n    global MAX\n    n = len(tree)\n    if root is None:\n     \
    \   hs = centroid(tree)\n    else:\n        hs = [root]\n    res = []\n    for\
    \ rt in hs:\n        tp_order, _ = topological_sorted(tree, rt)\n        visited\
    \ = [-1] * n\n        for v in tp_order[::-1]:\n            tmp = []\n       \
    \     for nxt_v in tree[v]:\n                if visited[nxt_v] == -1:\n      \
    \              continue\n                else:\n                    tmp.append(visited[nxt_v])\n\
    \            tmp = tuple(sorted(tmp))\n            if tmp not in HASHMAP:\n  \
    \              HASHMAP[tmp] = MAX\n                MAX += 1\n            visited[v]\
    \ = HASHMAP[tmp]\n        res.append(visited[rt])\n    res = tuple(sorted(res))\n\
    \    return res\n"
  dependsOn:
  - Graph/Tree/centroid.py
  - Graph/Tree/topological_sorted.py
  isVerificationFile: false
  path: Graph/Tree/treehash.py
  requiredBy: []
  timestamp: '2021-05-05 16:08:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/2821.test.py
documentation_of: Graph/Tree/treehash.py
layout: document
title: "\u6728\u306E\u30CF\u30C3\u30B7\u30E5 (\u6728\u306E\u540C\u578B\u5224\u5B9A\
  )"
---

## 概要
木のハッシュを求めるアルゴリズム。

## 使い方
`treehash(tree: Sequence[Iterable[int]], root: Union[int, None] = None) -> Tuple[int]`  
木 `tree` のハッシュ値を返す。ハッシュ値は、木の中心の数と同じサイズのタプルとなる。`root` を指定すると根付き木に対するハッシュとなる。計算量 $O(V \log V)$

## 参考
- https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf
- https://logic.pdmi.ras.ru/~smal/files/smal_jass08.pdf
- [木の同型性判定のお話 - kazu0x17’s diary](https://chocobaby-aporo.hatenablog.com/entry/2017/12/05/233027)