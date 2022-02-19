---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/LowLink.py
    title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS \u6728\u306E\
      \u69CB\u7BC9 (Low Link)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/two_edge_connected_components.test.py
    title: TestCase/LibraryChecker/two_edge_connected_components.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph.misc.LowLink import LowLink\n\n\nclass TwoEdgeConnectedComponents(LowLink):\n\
    \    def build(self):\n        super().build()\n        self.labels = [-1] * self.n\n\
    \        self.lb_cnt = 0\n        for v in range(self.n):\n            if self.labels[v]\
    \ != -1:\n                continue\n            self.labels[v] = self.lb_cnt\n\
    \            stack = [v]\n            while stack:\n                v = stack.pop()\n\
    \                for nxt_v in self.graph[v]:\n                    if self.ord[v]\
    \ < self.low[nxt_v] or self.ord[nxt_v] < self.low[v]:\n                      \
    \  continue\n                    if self.labels[nxt_v] != -1:\n              \
    \          continue\n                    self.labels[nxt_v] = self.lb_cnt\n  \
    \                  stack.append(nxt_v)\n            self.lb_cnt += 1\n\n    def\
    \ groups(self):\n        res = [[] for _ in range(self.lb_cnt)]\n        for v,\
    \ lb in enumerate(self.labels):\n            res[lb].append(v)\n        return\
    \ res\n"
  dependsOn:
  - Graph/misc/LowLink.py
  isVerificationFile: false
  path: Graph/Decomposition/TwoEdgeConnectedComponents.py
  requiredBy: []
  timestamp: '2021-01-28 21:03:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/two_edge_connected_components.test.py
documentation_of: Graph/Decomposition/TwoEdgeConnectedComponents.py
layout: document
title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
---

## 概要
無向グラフを二重辺連結成分分解するアルゴリズム。

## 使い方
`TwoEdgeConnectedComponents(n: int)`  
頂点数 `n` の辺のないグラフを構築する。計算量 $O(V)$

- `add_edge(u: int, v: int) -> None`  
頂点 `u` と頂点 `v` との間に無向辺を追加する。計算量 $O(1)$

- `build() -> None`  
二重辺連結成分分解を行う。`build` の実行後には、インスタンス変数である `labels` に各頂点の二重辺連結成分の番号が格納される。計算量 $O(V + E)$

- `groups() -> List[List[int]]`  
二重辺連結成分ごとに元の頂点を列挙する。計算量 $O(V)$
