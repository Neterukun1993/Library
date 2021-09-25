---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/lca.offline.test.py
    title: TestCase/LibraryChecker/lca.offline.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\n\n\ndef offline_lca(tree,\
    \ queries, root):\n    n = len(tree)\n    q = len(queries)\n    uf = UnionFind(n)\n\
    \    par = [-1] * n\n    anc = [-1] * n\n    ans = [-1] * q\n    qs = [[] for\
    \ i in range(n)]\n    for i, (u, v) in enumerate(queries):\n        qs[u].append((v\
    \ << 24) + i)\n        qs[v].append((u << 24) + i)\n\n    stack = [root]\n   \
    \ while stack:\n        v = stack.pop()\n        if v < 0:\n            v = ~v\n\
    \            for tmp in qs[v]:\n                nxt_v = tmp >> 24\n          \
    \      i = tmp - (nxt_v << 24)\n                ans[i] = anc[uf.root(nxt_v)]\n\
    \            uf.merge(par[v], v)\n            anc[uf.root(par[v])] = par[v]\n\
    \            continue\n        stack.append(~v)\n        for nxt_v in tree[v]:\n\
    \            if par[v] == nxt_v:\n                continue\n            par[nxt_v]\
    \ = v\n            stack.append(nxt_v)\n    return ans\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/Tree/offline_lca.py
  requiredBy: []
  timestamp: '2021-06-20 02:02:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/lca.offline.test.py
documentation_of: Graph/Tree/offline_lca.py
layout: document
title: "\u6700\u5C0F\u5171\u901A\u7956\u5148 (Tarjan \u306E\u30AA\u30D5\u30E9\u30A4\
  \u30F3\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0)"
---

## 概要
最小共通先祖クエリにオフラインで答えるアルゴリズム。

## 使い方
`offline_lca(tree: Sequence[Iterable[int]], queries: Sequence[Tuple[int, int]], root: int) -> List[int]`  
根が `root` である木 `tree` に対して LCA を求める。計算量 $O(V + Q)$

$i$ 番目のクエリ `queries[i]` の意味は次の通りである。
```
u v
```
頂点 $u$ と頂点 $v$ の LCA は何か？

## 参考
- [Lowest Common Ancestor - Tarjan's off-line algorithm - Competitive Programming Algorithms](https://cp-algorithms.com/graph/lca_tarjan.html)