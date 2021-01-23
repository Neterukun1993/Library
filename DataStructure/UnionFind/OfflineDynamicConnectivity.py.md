---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFindUndo.py
    title: "\u5DFB\u304D\u623B\u3057\u53EF\u80FDUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\2235.test.py
    title: TestCase\AOJ\2235.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFindUndo import UnionFindUndo\r\n\r\n\r\
    \nclass OfflineDynamicConnectivity:\r\n    def __init__(self, q, questions, n):\r\
    \n        self.q = q\r\n        self.questions = questions\r\n        self.n =\
    \ n\r\n        self.add_time = {}\r\n        self.exist = {}\r\n        self.pend\
    \ = []\r\n\r\n        self.size = 2 ** ((q - 1).bit_length())\r\n        self.node\
    \ = [[] for _ in range(2 * self.size)]\r\n        self.uf = UnionFindUndo(n)\r\
    \n\r\n    def insert(self, t, u, v):\r\n        \"\"\"insert (u, v) edge at time\
    \ t\"\"\"\r\n        if u > v:\r\n            u, v = v, u\r\n        uv = u *\
    \ self.n + v\r\n        self.add_time[uv] = t\r\n        self.exist[uv] = True\r\
    \n\r\n    def erase(self, t, u, v):\r\n        \"\"\"erase (u, v) edge at time\
    \ t\"\"\"\r\n        if u > v:\r\n            u, v = v, u\r\n        uv = u *\
    \ self.n + v\r\n        self.exist[uv] = False\r\n        self.pend.append((self.add_time[uv],\
    \ t, uv))\r\n\r\n    def construct(self):\r\n        \"\"\"construct query on\
    \ Segment Tree\"\"\"\r\n        for uv in self.exist:\r\n            if self.exist[uv]:\r\
    \n                self.pend.append((self.add_time[uv], self.q, uv))\r\n      \
    \  for l, r, uv in self.pend:\r\n            self._add(l, r, uv)\r\n\r\n    def\
    \ run(self):\r\n        \"\"\"run queries and get results\"\"\"\r\n        self.res\
    \ = []\r\n        self._dfs()\r\n        return self.res\r\n\r\n    def _add(self,\
    \ l, r, uv):\r\n        \"\"\"add (u, v) edge in [l, r) of Segment Tree\"\"\"\r\
    \n        l, r = l + self.size, r + self.size\r\n        while l < r:\r\n    \
    \        if l & 1:\r\n                self.node[l].append(uv)\r\n            \
    \    l += 1\r\n            if r & 1:\r\n                r -= 1\r\n           \
    \     self.node[r].append(uv)\r\n            l, r = l >> 1, r >> 1\r\n\r\n   \
    \ def _dfs(self, k=1):\r\n        \"\"\"DFS on Segment Tree\"\"\"\r\n        if\
    \ k >= self.size + self.q:\r\n            return\r\n        for uv in self.node[k]:\
    \  # pre-process\r\n            u, v = divmod(uv, self.n)\r\n            self.uf.merge(u,\
    \ v)\r\n\r\n        if k >= self.size:\r\n            self.res.append(self.uf.same(*self.questions[k\
    \ - self.size]))\r\n        else:\r\n            self._dfs(2 * k)\r\n        \
    \    self._dfs(2 * k + 1)\r\n\r\n        for _ in range(len(self.node[k])):  #\
    \ post-process\r\n            self.uf.undo()\r\n"
  dependsOn:
  - DataStructure\UnionFind\UnionFindUndo.py
  isVerificationFile: false
  path: DataStructure\UnionFind\OfflineDynamicConnectivity.py
  requiredBy: []
  timestamp: '2021-01-04 02:54:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\2235.test.py
documentation_of: DataStructure\UnionFind\OfflineDynamicConnectivity.py
layout: document
title: Offline Dynamic Connectivity
---
