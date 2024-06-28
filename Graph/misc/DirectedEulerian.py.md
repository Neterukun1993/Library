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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\n\n\nclass DirectedEulerian:\n\
    \    def __init__(self, n):\n        self.n = n\n        self.digraph = [[] for\
    \ i in range(n)]\n        self.diff = [0] * n   # diff = outdeg - indeg\n    \
    \    self.uf = UnionFind(n)\n\n    def add_edge(self, fr, to):\n        self.digraph[fr].append(to)\n\
    \        self.diff[fr] += 1\n        self.diff[to] -= 1\n        self.uf.merge(fr,\
    \ to)\n\n    def is_eulerian(self):\n        if self.uf.count() != 1:\n      \
    \      # \u30B0\u30E9\u30D5\u304C\u975E\u9023\u7D50\u306A\u3068\u304D\u306F False\
    \ \u3092\u8FD4\u3059\n            return False\n        return all(self.diff[v]\
    \ == 0 for v in range(self.n))\n\n    def is_semi_eulerian(self):\n        if\
    \ self.uf.count() != 1:\n            # \u30B0\u30E9\u30D5\u304C\u975E\u9023\u7D50\
    \u306A\u3068\u304D\u306F False \u3092\u8FD4\u3059\n            return False, -1,\
    \ -1\n        s = [v for v in range(self.n) if self.diff[v] == 1]\n        t =\
    \ [v for v in range(self.n) if self.diff[v] == -1]\n        if len(s) == 1 and\
    \ len(t) == 1:\n            return True, s[0], t[0]\n        return False, -1,\
    \ -1\n\n    def euler_path(self, start):\n        path = []\n        if self.is_eulerian()\
    \ or self.is_semi_eulerian()[0]:\n            idxs = [0] * self.n\n          \
    \  stack = [start]\n            while stack:\n                v = stack[-1]\n\
    \                if idxs[v] == len(self.digraph[v]):\n                    path.append(v)\n\
    \                    stack.pop()\n                else:\n                    nxt_v\
    \ = self.digraph[v][idxs[v]]\n                    stack.append(nxt_v)\n      \
    \              idxs[v] += 1\n            return True, path\n        return False,\
    \ path\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/misc/DirectedEulerian.py
  requiredBy: []
  timestamp: '2022-01-18 22:15:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/misc/DirectedEulerian.py
layout: document
title: "\u6709\u5411\u30B0\u30E9\u30D5\u306E\u30AA\u30A4\u30E9\u30FC\u8DEF"
---
