---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\nclass Dinic:\n    def __init__(self, n):\n\
    \        self.n = n\n        self.graph = [[] for _ in range(n)]\n\n    def add_edge(self,\
    \ fr, to, cap):\n        fr_idx = len(self.graph[fr])\n        to_idx = len(self.graph[to])\n\
    \        if fr == to:\n            to_idx += 1\n        self.graph[fr].append([to,\
    \ to_idx, cap])\n        self.graph[to].append([fr, fr_idx, 0])\n\n    def max_flow(self,\
    \ s, t):\n        def bfs():\n            level[s] = 0\n            q = deque([s])\n\
    \            while q:\n                v = q.popleft()\n                for to,\
    \ rev, cap in self.graph[v]:\n                    if cap == 0 or level[to] >=\
    \ 0:\n                        continue\n                    level[to] = level[v]\
    \ + 1\n                    if to == t:\n                        return\n     \
    \               q.append(to)\n\n        def dfs(up):\n            stack = [t]\n\
    \            while stack:\n                v = stack[-1]\n                if v\
    \ == s:\n                    stack.pop()\n                    flow = up\n    \
    \                for v in stack:\n                        to, rev, cap = self.graph[v][itr[v]]\n\
    \                        flow = min(flow, self.graph[to][rev][2])\n          \
    \          for v in stack:\n                        self.graph[v][itr[v]][2] +=\
    \ flow\n                        to, rev, cap = self.graph[v][itr[v]]\n       \
    \                 self.graph[to][rev][2] -= flow\n                    return flow\n\
    \                lv = level[v]\n                while itr[v] < len(self.graph[v]):\n\
    \                    to, rev, cap = self.graph[v][itr[v]]\n                  \
    \  if lv <= level[to] or self.graph[to][rev][2] == 0:\n                      \
    \  itr[v] += 1\n                        continue\n                    stack.append(to)\n\
    \                    break\n                if itr[v] == len(self.graph[v]):\n\
    \                    stack.pop()\n                    level[v] = self.n\n    \
    \        return 0\n\n        limit = 10 ** 9 + 7\n        flow = 0\n        while\
    \ flow < limit:\n            level = [-1] * self.n\n            bfs()\n      \
    \      if level[t] == -1:\n                break\n            itr = [0] * self.n\n\
    \            while flow < limit:\n                f = dfs(limit - flow)\n    \
    \            if f == 0:\n                    break\n                flow += f\n\
    \        return flow\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/Dinic.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Flow/Dinic.py
layout: document
redirect_from:
- /library/Flow/Dinic.py
- /library/Flow/Dinic.py.html
title: Flow/Dinic.py
---
