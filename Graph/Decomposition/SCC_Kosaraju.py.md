---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
    title: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/scc.Kosaraju.test.py
    title: TestCase/LibraryChecker/scc.Kosaraju.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class StronglyConnectedComponents:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.graph = [[] for _ in range(n)]\n        self.rev_graph = [[]\
    \ for _ in range(n)]\n        self.labels = [-1] * n\n        self.lb_cnt = 0\n\
    \n    def add_edge(self, v, nxt_v):\n        self.graph[v].append(nxt_v)\n   \
    \     self.rev_graph[nxt_v].append(v)\n\n    def build(self):\n        self.post_order\
    \ = []\n        self.used = [False] * self.n\n        for v in range(self.n):\n\
    \            if not self.used[v]:\n                self._dfs(v)\n\n        for\
    \ v in reversed(self.post_order):\n            if self.labels[v] == -1:\n    \
    \            self._rev_dfs(v)\n                self.lb_cnt += 1\n\n    def _dfs(self,\
    \ v):\n        stack = [v, 0]\n        while stack:\n            v, idx = stack[-2:]\n\
    \            if not idx and self.used[v]:\n                stack.pop()\n     \
    \           stack.pop()\n            else:\n                self.used[v] = True\n\
    \                if idx < len(self.graph[v]):\n                    stack[-1] +=\
    \ 1\n                    stack.append(self.graph[v][idx])\n                  \
    \  stack.append(0)\n                else:\n                    stack.pop()\n \
    \                   self.post_order.append(stack.pop())\n\n    def _rev_dfs(self,\
    \ v):\n        stack = [v]\n        self.labels[v] = self.lb_cnt\n        while\
    \ stack:\n            v = stack.pop()\n            for nxt_v in self.rev_graph[v]:\n\
    \                if self.labels[nxt_v] != -1:\n                    continue\n\
    \                stack.append(nxt_v)\n                self.labels[nxt_v] = self.lb_cnt\n\
    \n    def construct_dag(self):\n        self.dag = [[] for i in range(self.lb_cnt)]\n\
    \        self.groups = [[] for i in range(self.lb_cnt)]\n        for v, lb in\
    \ enumerate(self.labels):\n            for nxt_v in self.graph[v]:\n         \
    \       nxt_lb = self.labels[nxt_v]\n                if lb == nxt_lb:\n      \
    \              continue\n                self.dag[lb].append(nxt_lb)\n       \
    \     self.groups[lb].append(v)\n        return self.dag, self.groups\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Decomposition/SCC_Kosaraju.py
  requiredBy: []
  timestamp: '2021-01-09 01:09:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_3_C.Kosaraju.test.py
  - TestCase/LibraryChecker/scc.Kosaraju.test.py
documentation_of: Graph/Decomposition/SCC_Kosaraju.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\u30B4\
  \u30EA\u30BA\u30E0)"
---

## 概要
有向グラフを強連結成分分解するアルゴリズム。

## 使い方
`StronglyConnectedComponents(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(v: int, nxt_v: int) -> None`  
頂点 `v` から 頂点 `nxt_v` への有向辺を追加する。計算量 $O(1)$

- `build() -> None`  
強連結成分分解を行う。`build` の実行後には、インスタンス変数である `labels` に各頂点の強連結成分の番号 (縮約後の頂点番号) が格納される。縮約後の頂点番号はトポロジカルソート順である。計算量 $O(V + E)$

- `construct_dag() -> Tuple[List[List[int]], List[int]]`  
縮約後の頂点による有向グラフと、縮約後の頂点が含む元の頂点を返す。計算量 $O(V + E)$
