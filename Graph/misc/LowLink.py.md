---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/Decomposition/TwoEdgeConnectedComponents.py
    title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_3_A.test.py
    title: TestCase/AOJ/GRL_3_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_3_B.test.py
    title: TestCase/AOJ/GRL_3_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LowLink:\n    def __init__(self, n):\n        self.n = n\n        self.graph\
    \ = [[] for _ in range(n)]\n        self.dfstree = [[] for _ in range(n)]\n  \
    \      self.par = [-1] * n\n        self.ord = [-1] * n\n        self.low = [-1]\
    \ * n\n        self.articulations = []\n        self.bridges = []\n        self.roots\
    \ = set()\n\n    def add_edge(self, u, v):\n        self.graph[u].append(v)\n\
    \        self.graph[v].append(u)\n\n    def build(self):\n        k = 0\n    \
    \    self.edge_cnt = {}\n        for v in range(self.n):\n            for nxt_v\
    \ in self.graph[v]:\n                self.edge_cnt[v, nxt_v] = self.edge_cnt.get((v,\
    \ nxt_v), 0) + 1\n        idxs = [0] * self.n\n        arts = [False] * self.n\n\
    \        for v in range(self.n):\n            if self.ord[v] == -1:\n        \
    \        self.roots.add(v)\n                k = self._dfs(v, idxs, arts, k)\n\n\
    \    def _dfs(self, root, idxs, arts, k):\n        stack = [root]\n        while\
    \ stack:\n            v = stack[-1]\n            if v < 0:\n                v\
    \ = ~v\n                par_v = self.par[v]\n                self.low[par_v] =\
    \ min(self.low[par_v], self.low[v])\n                arts[par_v] |= (self.par[par_v]\
    \ != -1 and self.ord[par_v] <= self.low[v])\n                if self.ord[par_v]\
    \ < self.low[v]:\n                    self.bridges.append((par_v, v))\n      \
    \          stack.pop()\n                continue\n            idx = idxs[v]\n\
    \            if self.ord[v] == -1:\n                self.ord[v] = self.low[v]\
    \ = k\n                k += 1\n            if idx < len(self.graph[v]):\n    \
    \            nxt_v = self.graph[v][idx]\n                idxs[v] += 1\n      \
    \          if nxt_v == self.par[v] and self.edge_cnt[v, nxt_v] == 1:\n       \
    \             continue \n                elif self.ord[nxt_v] == -1:\n       \
    \             self.dfstree[v].append(nxt_v)\n                    self.dfstree[nxt_v].append(v)\n\
    \                    self.par[nxt_v] = v\n                    stack.append(~nxt_v)\n\
    \                    stack.append(nxt_v)\n                else:\n            \
    \        self.low[v] = min(self.low[v], self.ord[nxt_v])\n            else:\n\
    \                arts[v] |= (root == v and len(self.dfstree[v]) >= 2)\n      \
    \          if arts[v]:\n                    self.articulations.append(v)\n   \
    \             stack.pop()\n        return k\n\n    def enumerate_articulations(self):\n\
    \        for v in self.articulations:\n            yield v\n\n    def enumerate_bridges(self):\n\
    \        for u, v in self.bridges:\n            yield u, v\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/LowLink.py
  requiredBy:
  - Graph/Decomposition/TwoEdgeConnectedComponents.py
  timestamp: '2021-01-25 22:00:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_3_B.test.py
  - TestCase/AOJ/GRL_3_A.test.py
documentation_of: Graph/misc/LowLink.py
layout: document
title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS \u6728\u306E\u69CB\
  \u7BC9 (Low Link)"
---

## 概要
無向グラフに対して DFS 木を構築する。関節点・橋の列挙が可能。

## 使い方
`LowLink(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(u: int, v: int) -> None`  
頂点 `u` と 頂点 `v` との間に無向辺を追加する。計算量 $O(1)$

- `build() -> None`  
Low Link のアルゴリズムによって DFS 木を構築する。計算量 $O(V + E)$

- `enumerate_articulations() -> Iterator[int]`  
関節点を返すイテレータを返す。1 要素のイテレートにかかる計算量 $O(1)$

- `enumerate_bridges() -> Iterator[Tuple[int, int]]`  
橋を返すイテレータを返す。1 要素のイテレートにかかる計算量 $O(1)$
