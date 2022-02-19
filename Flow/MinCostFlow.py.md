---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_6_B.test.py
    title: TestCase/AOJ/GRL_6_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from heapq import heappush, heappop\nfrom standard_library.heapq import\
    \ heappush, heappop\n\n\nclass MinCostFlow:\n    def __init__(self, n):\n    \
    \    self.INF = 10 ** 9 + 7\n        self.n = n\n        self.graph = [[] for\
    \ _ in range(n)]\n\n    def add_edge(self, fr, to, cap, cost):\n        fr_idx\
    \ = len(self.graph[fr])\n        to_idx = len(self.graph[to])\n        if fr ==\
    \ to:\n            to_idx += 1\n        self.graph[fr].append([to, to_idx, cap,\
    \ cost])\n        self.graph[to].append([fr, fr_idx, 0, -cost])\n\n    def min_cost_flow(self,\
    \ s, t, flow) -> int:\n        res = 0\n        potential = [0] * self.n\n   \
    \     prv_v = [0] * self.n\n        prv_e = [None] * self.n\n        while flow\
    \ > 0:\n            # \u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u3092\u7528\u3044\u305F\
    \u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5\n            dist = [self.INF] * self.n\n\
    \            dist[s] = 0\n            q = [(0, s)]  # q = [(s\u304B\u3089\u306E\
    \u30B3\u30B9\u30C8, \u73FE\u5728\u5730)]\n            while q:\n             \
    \   cost, fr = heappop(q)\n                if dist[fr] < cost:\n             \
    \       continue\n                for edge in self.graph[fr]:\n              \
    \      to, _, cap, cost = edge\n                    p_diff = potential[fr] - potential[to]\n\
    \                    if cap > 0 and dist[fr] + cost + p_diff < dist[to]:\n   \
    \                     dist[to] = dist[fr] + cost + p_diff\n                  \
    \      prv_v[to] = fr\n                        prv_e[to] = edge\n            \
    \            heappush(q, (dist[to], to))\n\n            if dist[t] == self.INF:\n\
    \                return -1\n            for i in range(self.n):\n            \
    \    if dist[i] != self.INF:\n                    potential[i] += dist[i]\n  \
    \          d = flow\n            v = t\n            while v != s:\n          \
    \      d = min(d, prv_e[v][2])\n                v = prv_v[v]\n            flow\
    \ -= d\n            res += potential[t] * d\n            v = t\n            while\
    \ v != s:\n                edge = prv_e[v]\n                edge[2] -= d\n   \
    \             self.graph[edge[0]][edge[1]][2] += d\n                v = prv_v[v]\n\
    \        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/MinCostFlow.py
  requiredBy: []
  timestamp: '2022-01-20 17:35:30+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_6_B.test.py
documentation_of: Flow/MinCostFlow.py
layout: document
title: "\u6700\u5C0F\u8CBB\u7528\u6D41 (Primal-Dual \u6CD5)"
---
