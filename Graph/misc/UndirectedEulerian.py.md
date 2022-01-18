---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\n\n\nclass UndirectedEulerian:\n\
    \    def __init__(self, n):\n        self.n = n\n        self.graph = [[] for\
    \ i in range(n)]\n        self.deg = [0] * n\n        self.uf = UnionFind(n)\n\
    \n    def add_edge(self, u, v):\n        u_idx = len(self.graph[u])\n        v_idx\
    \ = len(self.graph[v])\n        if u == v:\n            v_idx += 1\n        self.graph[u].append((v,\
    \ v_idx))\n        self.graph[v].append((u, u_idx))\n        self.deg[u] += 1\n\
    \        self.deg[v] += 1\n        self.uf.merge(u, v)\n\n    def is_eulerian(self):\n\
    \        if self.uf.count() != 1:\n            # \u30B0\u30E9\u30D5\u304C\u975E\
    \u9023\u7D50\u306A\u3068\u304D\u306F False \u3092\u8FD4\u3059\n            return\
    \ False\n        return all(self.deg[v] % 2 == 0 for v in range(self.n))\n\n \
    \   def is_semi_eulerian(self):\n        if self.uf.count() != 1:\n          \
    \  # \u30B0\u30E9\u30D5\u304C\u975E\u9023\u7D50\u306A\u3068\u304D\u306F False\
    \ \u3092\u8FD4\u3059\n            return False, -1, -1\n        s = [v for v in\
    \ range(self.n) if self.deg[v] % 2 == 1]\n        if len(s) == 2:\n          \
    \  return True, s[0], s[1]\n        return False, -1, -1\n\n    def euler_path(self,\
    \ start):\n        path = []\n        semi, s, t = self.is_semi_eulerian()\n \
    \       if self.is_eulerian() or s == start or t == start:\n            idxs =\
    \ [0] * self.n\n            used = [[False] * len(self.graph[v]) for v in range(self.n)]\n\
    \            stack = [start]\n            while stack:\n                v = stack[-1]\n\
    \                if idxs[v] == len(self.graph[v]):\n                    path.append(v)\n\
    \                    stack.pop()\n                else:\n                    idx\
    \ = idxs[v]\n                    nxt_v, nxt_idx = self.graph[v][idx]\n       \
    \             if not used[v][idx]:\n                        used[v][idx] = True\n\
    \                        used[nxt_v][nxt_idx] = True\n                       \
    \ stack.append(nxt_v)\n                    idxs[v] += 1\n            return True,\
    \ path\n        else:\n            return False, path\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/misc/UndirectedEulerian.py
  requiredBy: []
  timestamp: '2022-01-18 22:15:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/misc/UndirectedEulerian.py
layout: document
title: "\u7121\u5411\u30B0\u30E9\u30D5\u306E\u30AA\u30A4\u30E9\u30FC\u8DEF"
---
