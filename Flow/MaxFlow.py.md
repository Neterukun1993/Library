---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2313.test.py
    title: TestCase/AOJ/2313.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_6_A.dinic.test.py
    title: TestCase/AOJ/GRL_6_A.dinic.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class MaxFlow:\n    def __init__(self, n):\n        self.n = n\n        self.graph\
    \ = [[] for _ in range(n)]\n        self.pos = []\n\n    def add_edge(self, fr,\
    \ to, cap):\n        assert(0 <= fr < self.n)\n        assert(0 <= to < self.n)\n\
    \        assert(0 <= cap)\n        fr_idx = len(self.graph[fr])\n        to_idx\
    \ = len(self.graph[to])\n        if fr == to:\n            to_idx += 1\n     \
    \   self.pos.append([fr, fr_idx])\n        self.graph[fr].append([to, to_idx,\
    \ cap])\n        self.graph[to].append([fr, fr_idx, 0])\n\n    def get_edge(self,\
    \ i):\n        assert(0 <= i < len(self.pos))\n        edge = self.graph[self.pos[i][0]][self.pos[i][1]]\n\
    \        rev_edge = self.graph[edge[0]][edge[1]]\n        return (self.pos[i][0],\
    \ edge[0], edge[2] + rev_edge[2], rev_edge[2])\n\n    def edges(self):\n     \
    \   return [self.get_edge(i) for i in range(len(self.pos))]\n\n    def change_edge(self,\
    \ i, new_cap, new_flow):\n        assert(0 <= i < len(self.pos))\n        assert(0\
    \ <= new_flow <= new_cap)\n        edge = self.graph[self.pos[i][0]][self.pos[i][1]]\n\
    \        rev_edge = self.graph[edge[0]][edge[1]]\n        edge[2] = new_cap -\
    \ new_flow\n        rev_edge[2] = new_flow\n\n    def max_flow(self, s, t, flow_limit):\n\
    \        assert(0 <= s < self.n)\n        assert(0 <= s < self.n)\n        assert(s\
    \ != t)\n\n        def bfs():\n            level[s] = 0\n            q = [s]\n\
    \            head = 0\n            while head < len(q):\n                v = q[head]\n\
    \                head += 1\n                for to, rev, cap in self.graph[v]:\n\
    \                    if cap == 0 or level[to] >= 0:\n                        continue\n\
    \                    level[to] = level[v] + 1\n                    if to == t:\n\
    \                        return\n                    q.append(to)\n\n        def\
    \ dfs(up):\n            stack = [t]\n            while stack:\n              \
    \  v = stack[-1]\n                if v == s:\n                    stack.pop()\n\
    \                    flow = up\n                    for v in stack:\n        \
    \                to, rev, _ = self.graph[v][itr[v]]\n                        flow\
    \ = min(flow, self.graph[to][rev][2])\n                    for v in stack:\n \
    \                       self.graph[v][itr[v]][2] += flow\n                   \
    \     to, rev, _ = self.graph[v][itr[v]]\n                        self.graph[to][rev][2]\
    \ -= flow\n                    return flow\n                lv = level[v]\n  \
    \              while itr[v] < len(self.graph[v]):\n                    to, rev,\
    \ _ = self.graph[v][itr[v]]\n                    if lv <= level[to] or self.graph[to][rev][2]\
    \ == 0:\n                        itr[v] += 1\n                        continue\n\
    \                    stack.append(to)\n                    break\n           \
    \     if itr[v] == len(self.graph[v]):\n                    stack.pop()\n    \
    \                level[v] = self.n\n            return 0\n\n        flow = 0\n\
    \        while flow < flow_limit:\n            level = [-1] * self.n\n       \
    \     bfs()\n            if level[t] == -1:\n                break\n         \
    \   itr = [0] * self.n\n            while flow < flow_limit:\n               \
    \ f = dfs(flow_limit - flow)\n                if f == 0:\n                   \
    \ break\n                flow += f\n        return flow\n\n    def min_cut(self,\
    \ s):\n        assert(0 <= s < self.n)\n        visited = [False] * self.n\n \
    \       stack = [s]\n        visited[s] = True\n        while stack:\n       \
    \     v = stack.pop()\n            for to, _, cap in self.graph[v]:\n        \
    \        if cap > 0 and not visited[to]:\n                    visited[to] = True\n\
    \                    stack.append(to)\n        return visited\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/MaxFlow.py
  requiredBy: []
  timestamp: '2022-01-04 20:45:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/2313.test.py
  - TestCase/AOJ/GRL_6_A.dinic.test.py
documentation_of: Flow/MaxFlow.py
layout: document
title: "\u6700\u5927\u6D41 (Dinic \u6CD5)"
---
